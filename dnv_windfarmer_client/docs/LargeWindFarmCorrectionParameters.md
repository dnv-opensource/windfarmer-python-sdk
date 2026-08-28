# LargeWindFarmCorrectionParameters

The large wind farm correction parameter values.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**base_roughness_z01** | **float** | Base Roughness Z01. | [optional] 
**increased_roughness_z02** | **float** | Increased Roughness Z02. | [optional] 
**geometric_width_diameters** | **float** | Geometric Width Diameters. | [optional] [default to 1]
**recovery_start_diameters** | **float** | Recovery Start Diameters. | [optional] [default to 60]
**fifty_percent_recovery_diameters** | **float** | Fifty Percent Recovery Diameters. | [optional] [default to 40]

## Example

```python
from dnv_windfarmer_client.models.large_wind_farm_correction_parameters import LargeWindFarmCorrectionParameters

# TODO update the JSON string below
json = "{}"
# create an instance of LargeWindFarmCorrectionParameters from a JSON string
large_wind_farm_correction_parameters_instance = LargeWindFarmCorrectionParameters.from_json(json)
# print the JSON string representation of the object
print(LargeWindFarmCorrectionParameters.to_json())

# convert the object into a dict
large_wind_farm_correction_parameters_dict = large_wind_farm_correction_parameters_instance.to_dict()
# create an instance of LargeWindFarmCorrectionParameters from a dict
large_wind_farm_correction_parameters_from_dict = LargeWindFarmCorrectionParameters.from_dict(large_wind_farm_correction_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


