# AtmosphericConditionClass

An atmospheric condition class.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | A unique atmospheric condition profile identifier. | 
**boundary_layer_height_m** | **float** | Boundary layer height. Units: m | 
**lapse_rate_k_per_100m** | **float** | Lapse rate in free atmosphere. Units: K/100m | 
**delta_theta_across_inversion_layer_k** | **float** | Change in potential temperature across inversion layer. Units: K | 
**thickness_inversion_layer_m** | **float** | Thickness of inversion layer. Units: m | 
**heights_above_surface_m** | **List[float]** | Heights above surface for which the List&amp;lt;double&amp;gt; AtmosphericConditionClass.TurbulenceIntensityProfile and List&amp;lt;double&amp;gt; AtmosphericConditionClass.WindSpeedVerticalGradientProfile profile parameters are defined.  Requires 2 or more elements that must be sorted in increasing order and cannot be negative. Units: m | 
**turbulence_intensity_profile** | **List[float]** | Turbulence intensity profile at heights defined in List&amp;lt;double&amp;gt; AtmosphericConditionClass.HeightsAboveSurface. Must have the same length as height above surface list. Units: fraction of mean wind speed (0 to 1) | 
**wind_speed_vertical_gradient_profile_per_s_m** | **List[float]** | Wind speed vertical gradient profile at heights defined in List&amp;lt;double&amp;gt; AtmosphericConditionClass.HeightsAboveSurface. Must have the same length as height above surface list. Units: 1/s.m | 

## Example

```python
from dnv_windfarmer_client.models.atmospheric_condition_class import AtmosphericConditionClass

# TODO update the JSON string below
json = "{}"
# create an instance of AtmosphericConditionClass from a JSON string
atmospheric_condition_class_instance = AtmosphericConditionClass.from_json(json)
# print the JSON string representation of the object
print(AtmosphericConditionClass.to_json())

# convert the object into a dict
atmospheric_condition_class_dict = atmospheric_condition_class_instance.to_dict()
# create an instance of AtmosphericConditionClass from a dict
atmospheric_condition_class_from_dict = AtmosphericConditionClass.from_dict(atmospheric_condition_class_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


