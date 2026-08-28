# AnnualEnergyProductionJobStatus

Returns the status of an async AnnualEnergyProduction calculation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**progress** | **float** | Gets the calculation progress, as a percentage between 0 and 100. | [optional] 
**message** | **str** | Gets a status message for the calculation as a whole. | [optional] 
**stage_message** | **str** | Gets a status message for the current stage of the calculation. | [optional] 
**status** | [**CalculationStatus**](CalculationStatus.md) | Gets the calculation status (e.g. Pending, Executing, Faulted, Completed. | [optional] 
**results** | [**AnnualEnergyProductionResults**](AnnualEnergyProductionResults.md) | Gets the results of a completed calculation. | [optional] 
**results_stream** | **bytes** | Gets a stream which can be used to retrieve the calculation results. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.annual_energy_production_job_status import AnnualEnergyProductionJobStatus

# TODO update the JSON string below
json = "{}"
# create an instance of AnnualEnergyProductionJobStatus from a JSON string
annual_energy_production_job_status_instance = AnnualEnergyProductionJobStatus.from_json(json)
# print the JSON string representation of the object
print(AnnualEnergyProductionJobStatus.to_json())

# convert the object into a dict
annual_energy_production_job_status_dict = annual_energy_production_job_status_instance.to_dict()
# create an instance of AnnualEnergyProductionJobStatus from a dict
annual_energy_production_job_status_from_dict = AnnualEnergyProductionJobStatus.from_dict(annual_energy_production_job_status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


