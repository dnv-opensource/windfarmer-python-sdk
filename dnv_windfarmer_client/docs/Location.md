# Location

Represent the 3D properties of a site location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**easting_m** | **float** | Gets the easting. Units: m. | [optional] 
**northing_m** | **float** | Gets the northing. Units: m. | [optional] 
**terrain_height_above_sea_level_m** | **float** | Gets the height above sea level. Units: m. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.location import Location

# TODO update the JSON string below
json = "{}"
# create an instance of Location from a JSON string
location_instance = Location.from_json(json)
# print the JSON string representation of the object
print(Location.to_json())

# convert the object into a dict
location_dict = location_instance.to_dict()
# create an instance of Location from a dict
location_from_dict = Location.from_dict(location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


