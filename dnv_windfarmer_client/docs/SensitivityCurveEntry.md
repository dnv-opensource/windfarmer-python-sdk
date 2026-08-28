# SensitivityCurveEntry

A class for holding a sensitivity curve entry.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wind_speed_perturbation** | **float** | Gets or sets the WindSpeedPerturbation | [optional] 
**power_mw** | **float** | Gets or sets the power in MW. | [optional] 
**energy_perturbation** | **float** | Gets or sets the EnergyPerturbation | [optional] 

## Example

```python
from dnv_windfarmer_client.models.sensitivity_curve_entry import SensitivityCurveEntry

# TODO update the JSON string below
json = "{}"
# create an instance of SensitivityCurveEntry from a JSON string
sensitivity_curve_entry_instance = SensitivityCurveEntry.from_json(json)
# print the JSON string representation of the object
print(SensitivityCurveEntry.to_json())

# convert the object into a dict
sensitivity_curve_entry_dict = sensitivity_curve_entry_instance.to_dict()
# create an instance of SensitivityCurveEntry from a dict
sensitivity_curve_entry_from_dict = SensitivityCurveEntry.from_dict(sensitivity_curve_entry_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


