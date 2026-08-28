import os
import time
from pprint import pprint

from progressbar import ProgressBar

from dnv_windfarmer_client import (
    AnnualEnergyProductionApi,
    AnnualEnergyProductionAsyncApi,
    AnnualEnergyProductionJobStatus,
    AnnualEnergyProductionResults,
    ApiClient,
    ApiException,
    AtmosphericConditionsApi,
    BlockageModelType,
    CalculationQueuedResult,
    CalculationStatus,
    ComprehensiveSiteClassification,
    Configuration,
    EnergyCalculationInputs,
    Status,
    StatusApi,
    WakeModelType,
)

WINDFARMER_ACCESS_KEY_ENV_VAR = "WINDFARMER_ACCESS_KEY"
"""
The name of the environment variable containing the API access key. Default: WINDFARMER_ACCESS_KEY.
"""

WINDFARMER_ACCESS_KEY: str = None
"""
Set this to use a specific API access key. If this is not set, the key will be taken from the environment
variable set in WINDFARMER_ACCESS_KEY_ENV_VAR.
"""

API_URL: str = 'https://windfarmer.dnv.com/api/v3'
"""
The URL of the WindFarmer Services API
"""

def status() -> Status:
    """
    Gets the API status, including version numbers.
    """
    with ApiClient(_create_config()) as api_client:
        # Create an instance of the API class
        api_instance: StatusApi = StatusApi(api_client)

        # Get the status of the WindFarmer API
        api_response = api_instance.status_get()
        return api_response

def annual_energy_production_sync(energy_calculation_inputs: EnergyCalculationInputs) -> AnnualEnergyProductionResults:
    """
    Calls the synchronous Annual Energy Production API endpoint. This should only be used for quick calculations.
    """
    with ApiClient(_create_config()) as api_client:
        # Create an instance of the API class
        api_instance = AnnualEnergyProductionApi(api_client)

        # Post to the AnnualEnergyProductionApi
        api_response = api_instance.annual_energy_production_post(energy_calculation_inputs)
        return api_response

def annual_energy_production_async(energy_calculation_inputs: EnergyCalculationInputs) -> CalculationQueuedResult:
    """
    Queues a calculation using the asynchronous Annual Energy Production endpoint. Get the calculation status and results
    by calling job_status.
    """
    with ApiClient(_create_config()) as api_client:
        # Create an instance of the API class
        api_instance = AnnualEnergyProductionAsyncApi(api_client)

        # Post to the AnnualEnergyProductionApi
        api_response = api_instance.annual_energy_production_async_post(energy_calculation_inputs)
        return api_response

def annual_energy_production(
        energy_calculation_inputs: EnergyCalculationInputs) -> AnnualEnergyProductionResults:
    """
    Runs an Annual Energy Production calculation and waits for the results. If the calculation uses CFD.ML v2 then the 
    Atmospheric Conditions classification is retrieved from the AtmosphericConditions API.
    """
    # Call atmospheric conditions if cfdml
    if _is_cfdml_v2(energy_calculation_inputs):
        atmospheric_conditions_results = atmospheric_conditions(
            energy_calculation_inputs.project_info.site_latitude,
            energy_calculation_inputs.project_info.site_longitude)
        
        print("AEP calculation uses CFD.ML v2. Calculating atmospheric conditions")

        if not atmospheric_conditions_results:
            # TODO: Work out what our error handling strategy should be and how we communicated errors to users
            raise ApiException("Failed to get atmospheric conditions")

        energy_calculation_inputs.atmospheric_conditions = atmospheric_conditions_results.atmospheric_conditions

    # Send AEP calculation to the async endpoint
    queued_result = annual_energy_production_async(energy_calculation_inputs)

    # Wait for calculation to complete, and get results
    aep_results = wait_for_completion(queued_result, _calculate_poll_interval(energy_calculation_inputs))
    return aep_results.results

def atmospheric_conditions(
        latitude: float,
        longitude: float,
        radius_km: float = 50.0,
        land_fraction_threshold: float = 0.2) -> ComprehensiveSiteClassification:
    """
    Gets the atmospheric conditions site classification for a location. The result can be used in CFDML calculations.
    """
    
    with ApiClient(_create_config()) as api_client:
        api_instance = AtmosphericConditionsApi(api_client)
        return api_instance.atmospheric_conditions_get(latitude, longitude, radius_km, land_fraction_threshold)

def get_job_status(queued_result: CalculationQueuedResult) -> AnnualEnergyProductionJobStatus:
    """
    Gets the status of a job that was queued with annual_energy_production_async,
    """
    with ApiClient(_create_config()) as api_client:
        api_instance = AnnualEnergyProductionAsyncApi(api_client)
        return api_instance.annual_energy_production_async_get(queued_result.job_id)
         
def wait_for_completion(
        queued_result: CalculationQueuedResult,
        polling_interval_s: float = 5,
        timeout_s: float = 3600) -> AnnualEnergyProductionJobStatus:
    """
    Waits for a queued job to complete, and returns the results. 
    """
    iteration_count: int = 1
    job_status: AnnualEnergyProductionJobStatus = AnnualEnergyProductionJobStatus(status=CalculationStatus.PENDING)
    start_time: float = time.time()
    consecutive_errors: int = 0

    with ApiClient(_create_config()), ProgressBar(max_value=100, prefix='Progress', redirect_stdout=True) as bar:
        while (job_status.status == CalculationStatus.PENDING or job_status.status == CalculationStatus.RUNNING) and (time.time() - start_time) < timeout_s:
            time.sleep(polling_interval_s)
            try:
                iteration_count += 1
                job_status = get_job_status(queued_result)
                consecutive_errors = 0
                msg = ' - '.join(filter(None, [job_status.status, job_status.message, job_status.stage_message]))
                print(f'\r{iteration_count} {msg}')
                bar.update(job_status.progress)
            except ApiException as err:
                consecutive_errors += 1
                pprint(err)
                if (consecutive_errors > 3):
                    print("Quitting after 3 consecutive errors")
                raise
            
    if job_status.status == CalculationStatus.SUCCESS:
        print("Job completed successfully")
        return job_status
    elif job_status.status == CalculationStatus.FAILED:
            print("Job failed")
            raise ApiException(reason = job_status.message)
    elif job_status.status == CalculationStatus.CANCELLED:
            print("Job was cancelled")
            raise ApiException(reason = "Job cancelled")

    elif time.time() - start_time > timeout_s:
            raise ApiException(reason = f"Calculation timed out after {timeout_s} seconds.")
                 
def _calculate_poll_interval(inputs: EnergyCalculationInputs) -> float:
    turbine_count: int = 0
    for farm in inputs.wind_farms:
        turbine_count += len(farm.turbines)

    time_per_turbine = 1.2 # seconds
    return turbine_count * time_per_turbine / 5
 
def _is_cfdml_v2(inputs: EnergyCalculationInputs) -> bool:
    return inputs.energy_efficiencies_settings.wake_model.wake_model_type == WakeModelType.CFDML \
        and inputs.energy_efficiencies_settings.wake_model.cfdml.gnn_version.startswith('2.') \
        or inputs.energy_efficiencies_settings.blockage_model.blockage_model_type == BlockageModelType.CFDML \
        and inputs.energy_efficiencies_settings.blockage_model.cfdml.cfdml_settings.gnn_version.startswith('2.')

def _create_config():
    if not API_URL or API_URL == '':
        raise ValueError(f'The api_url has not been set. Omit this argument to use the default of {API_URL}.')

    access_key = WINDFARMER_ACCESS_KEY or os.environ.get(WINDFARMER_ACCESS_KEY_ENV_VAR)

    if not access_key or access_key == '':
            raise ValueError(
                f'The API access key has not been set. You should either:\n' \
                f'- Store the API access token in the {WINDFARMER_ACCESS_KEY_ENV_VAR} environment variable\n' \
                f'- Set windfarmer.WINDFARMER_ACCESS_KEY to you API access key\n'
                f'- Set windfarmer.WINDFARMER_ACCESS_KEY_ENV_VAR to the name of an environment variable that contains your API access key.')
    
    return Configuration(host=API_URL, access_token=access_key)
