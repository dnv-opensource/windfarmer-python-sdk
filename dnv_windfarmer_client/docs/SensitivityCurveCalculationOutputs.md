# SensitivityCurveCalculationOutputs

A class for holding the sensitivity curve calculation results.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**overall_sensitivity_curve** | [**OverallSensitivityCurve**](OverallSensitivityCurve.md) | Gets or sets the overall sensitivity curve DTO. | [optional] 
**wind_climate_sensitivity_curves** | [**List[WindClimateSensitivityCurve]**](WindClimateSensitivityCurve.md) | Gets or sets the wind climate sensitivity curve DTOs. | [optional] 
**turbine_sensitivity_curves** | [**List[TurbineSensitivityCurve]**](TurbineSensitivityCurve.md) | Gets or sets the turbine climate sensitivity curve DTOs. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.sensitivity_curve_calculation_outputs import SensitivityCurveCalculationOutputs

# TODO update the JSON string below
json = "{}"
# create an instance of SensitivityCurveCalculationOutputs from a JSON string
sensitivity_curve_calculation_outputs_instance = SensitivityCurveCalculationOutputs.from_json(json)
# print the JSON string representation of the object
print(SensitivityCurveCalculationOutputs.to_json())

# convert the object into a dict
sensitivity_curve_calculation_outputs_dict = sensitivity_curve_calculation_outputs_instance.to_dict()
# create an instance of SensitivityCurveCalculationOutputs from a dict
sensitivity_curve_calculation_outputs_from_dict = SensitivityCurveCalculationOutputs.from_dict(sensitivity_curve_calculation_outputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


