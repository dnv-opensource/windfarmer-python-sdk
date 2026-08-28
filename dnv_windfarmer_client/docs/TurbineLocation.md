# TurbineLocation

The turbine position and dimensions.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**easting_m** | **float** | The East position of the turbine. Units: m. | [optional] 
**northing_m** | **float** | The North position of the turbine. Units: m. | [optional] 
**hub_height_m** | **float** | The hub height of the turbine. Units: m. | [optional] 
**rotor_diameter_m** | **float** | The rotor diameter. Units: m. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.turbine_location import TurbineLocation

# TODO update the JSON string below
json = "{}"
# create an instance of TurbineLocation from a JSON string
turbine_location_instance = TurbineLocation.from_json(json)
# print the JSON string representation of the object
print(TurbineLocation.to_json())

# convert the object into a dict
turbine_location_dict = turbine_location_instance.to_dict()
# create an instance of TurbineLocation from a dict
turbine_location_from_dict = TurbineLocation.from_dict(turbine_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


