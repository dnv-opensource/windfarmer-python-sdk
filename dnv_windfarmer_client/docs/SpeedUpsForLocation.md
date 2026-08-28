# SpeedUpsForLocation

The relative speedup data for one location. An instance of this class should always be part of a FlowModel

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique identifier for a flow model point. Used to match to a turbine or wind climate. Expected format is:   * For turbines: [WindFarm Name]space[Turbine Name]   * For Wind climates: The wind climate Id string WindClimate.Id or string WeibullWindClimate.Id | 
**easting_m** | **float** | Gets the easting. Units: m. | 
**northing_m** | **float** | Gets the northing. Units: m. | 
**height_above_ground_m** | **float** | Gets the height above ground. Units: m. | 
**speed_ups** | **List[float]** | The speedup values for each wind direction. | 
**is_target** | **bool** | Whether these speed ups refer to a target (usually turbine) or a source (usually measurement site).  For backwards compatibility this defaults: true | [optional] [default to True]

## Example

```python
from dnv_windfarmer_client.models.speed_ups_for_location import SpeedUpsForLocation

# TODO update the JSON string below
json = "{}"
# create an instance of SpeedUpsForLocation from a JSON string
speed_ups_for_location_instance = SpeedUpsForLocation.from_json(json)
# print the JSON string representation of the object
print(SpeedUpsForLocation.to_json())

# convert the object into a dict
speed_ups_for_location_dict = speed_ups_for_location_instance.to_dict()
# create an instance of SpeedUpsForLocation from a dict
speed_ups_for_location_from_dict = SpeedUpsForLocation.from_dict(speed_ups_for_location_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


