# OverallSensitivityCurve

A class for holding an overall sensitivity curve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**entries** | [**List[SensitivityCurveEntry]**](SensitivityCurveEntry.md) | Gets or sets the Entries | [optional] 

## Example

```python
from dnv_windfarmer_client.models.overall_sensitivity_curve import OverallSensitivityCurve

# TODO update the JSON string below
json = "{}"
# create an instance of OverallSensitivityCurve from a JSON string
overall_sensitivity_curve_instance = OverallSensitivityCurve.from_json(json)
# print the JSON string representation of the object
print(OverallSensitivityCurve.to_json())

# convert the object into a dict
overall_sensitivity_curve_dict = overall_sensitivity_curve_instance.to_dict()
# create an instance of OverallSensitivityCurve from a dict
overall_sensitivity_curve_from_dict = OverallSensitivityCurve.from_dict(overall_sensitivity_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


