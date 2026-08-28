# TurbineSensitivityCurve

A class for holding a wind climate sensitivity curve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wind_farm** | **str** | Gets or sets the wind farm name | [optional] 
**turbine** | **str** | Gets or sets the turbine name | [optional] 
**entries** | [**List[SensitivityCurveEntry]**](SensitivityCurveEntry.md) | Gets or sets the Entries | [optional] 

## Example

```python
from dnv_windfarmer_client.models.turbine_sensitivity_curve import TurbineSensitivityCurve

# TODO update the JSON string below
json = "{}"
# create an instance of TurbineSensitivityCurve from a JSON string
turbine_sensitivity_curve_instance = TurbineSensitivityCurve.from_json(json)
# print the JSON string representation of the object
print(TurbineSensitivityCurve.to_json())

# convert the object into a dict
turbine_sensitivity_curve_dict = turbine_sensitivity_curve_instance.to_dict()
# create an instance of TurbineSensitivityCurve from a dict
turbine_sensitivity_curve_from_dict = TurbineSensitivityCurve.from_dict(turbine_sensitivity_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


