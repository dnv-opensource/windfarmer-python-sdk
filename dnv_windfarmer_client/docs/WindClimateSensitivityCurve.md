# WindClimateSensitivityCurve

A class for holding a wind climate sensitivity curve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wind_climate_id** | **str** | Gets or sets the wind climate ID. | [optional] 
**entries** | [**List[SensitivityCurveEntry]**](SensitivityCurveEntry.md) | Gets or sets the Entries | [optional] 

## Example

```python
from dnv_windfarmer_client.models.wind_climate_sensitivity_curve import WindClimateSensitivityCurve

# TODO update the JSON string below
json = "{}"
# create an instance of WindClimateSensitivityCurve from a JSON string
wind_climate_sensitivity_curve_instance = WindClimateSensitivityCurve.from_json(json)
# print the JSON string representation of the object
print(WindClimateSensitivityCurve.to_json())

# convert the object into a dict
wind_climate_sensitivity_curve_dict = wind_climate_sensitivity_curve_instance.to_dict()
# create an instance of WindClimateSensitivityCurve from a dict
wind_climate_sensitivity_curve_from_dict = WindClimateSensitivityCurve.from_dict(wind_climate_sensitivity_curve_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


