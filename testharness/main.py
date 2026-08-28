import json
import os
import sys

import pydantic
import windfarmer as wf

from dnv_windfarmer_client import EnergyCalculationInputs, Status


def main():

    # Get the API status
    status: Status = wf.status()
    print(f"API Version: {status.wind_farmer_services_api_version}, Calculation Version: {status.calculation_library_version}, Message: {status.message}")
    print(f'Python version: {sys.version}')

    # Run an CFDMLv2 AEP calculation

    # Load the json file
    with open(os.path.join(os.path.dirname(__file__), 'data/TheBowl.json'), 'r') as f:
        calculation_data = json.load(f)

    # Deserialize into an EnergyCalculationInputs object
    energy_calculation_inputs = EnergyCalculationInputs.from_dict(calculation_data)

    # Test validation: site_longitude must be between -180 and 180
    try:
        energy_calculation_inputs.project_info.site_longitude = 360
    except pydantic.ValidationError as err:
        for e in err.errors():
            print(f'{e['loc'][0]}: {e['msg']}')

    print("Running AEP calculation")
    aep_results = wf.annual_energy_production(energy_calculation_inputs)

    # # Print an ASCII table showing the full_annual_energy_yield_mwh_per_year for each wind farm in the results
    print("Wind Farm AEP Results:")
    print(f"{'Wind Farm Name':<30} {'Full Annual Energy Yield (MWh/year)':<30}")
    for wind_farm_result in aep_results.wind_farm_aep_outputs:
        print(f"{wind_farm_result.wind_farm_name:<30} {wind_farm_result.full_annual_energy_yield_mwh_per_year:<30.2f}") 

if __name__ == "__main__":
    main()
