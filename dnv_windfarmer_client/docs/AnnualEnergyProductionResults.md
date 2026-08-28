# AnnualEnergyProductionResults

Results for the Annual Energy Production calculation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wind_farm_aep_outputs** | [**List[WindFarmAepOutput]**](WindFarmAepOutput.md) | Gets the wind farm annual energy production outputs. The wind farm annual energy production output collection. | [optional] 
**weighted_blockage_efficiency** | **float** | The energy weighted blockage efficiency, calculated over all subject wind farms A value generally between 0.0 and 1.0 representing the blockage correction efficiency | [optional] 
**sensitivity_curves** | [**SensitivityCurveCalculationOutputs**](SensitivityCurveCalculationOutputs.md) | Wind speed to energy perturbation sensitivty curve calculation results,  Returned only when the calculateSensitivityCurve calculation option is true | [optional] 
**blockage_model_intermediate_data** | [**BlockageModelIntermediateData**](BlockageModelIntermediateData.md) | Blockage model intermediate data. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.annual_energy_production_results import AnnualEnergyProductionResults

# TODO update the JSON string below
json = "{}"
# create an instance of AnnualEnergyProductionResults from a JSON string
annual_energy_production_results_instance = AnnualEnergyProductionResults.from_json(json)
# print the JSON string representation of the object
print(AnnualEnergyProductionResults.to_json())

# convert the object into a dict
annual_energy_production_results_dict = annual_energy_production_results_instance.to_dict()
# create an instance of AnnualEnergyProductionResults from a dict
annual_energy_production_results_from_dict = AnnualEnergyProductionResults.from_dict(annual_energy_production_results_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


