# BeetSettings

The Beet model settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**significant_atmospheric_stability** | **bool** | If true, There is significant atmospheric stability, if false the atmosphere is predominantly neutral or unstable. | [optional] 
**include_intermediate_results** | **bool** | Gets or sets whether to include intermediate result data or not. | [optional] [default to False]
**inclusion_of_neighbors_buffer_zone_in_meters** | **float** | Inclusion buffer for neighboring wind farms to be included in estimating blockage for the subject farm; units: meters Note: property only relevant when CalculateBlockage &#x3D;&#x3D; true, and BlockageCorrectionApplicationMethod &#x3D;&#x3D; OnWindSpeed.       However, when BlockageApplicationMethod &#x3D;&#x3D; OnWindSpeed, the inclusion buffer needs to be set explicitly (may be 0 if all neighbours are to be excluded). | 
**blockage_correction_application_method** | [**BlockageCorrectionApplicationMethod**](BlockageCorrectionApplicationMethod.md) | Setting to specify whether to apply blockage correction on wind speed or on energy. Default value: OnEnergy.  Note: if includeBlockage &#x3D;&#x3D; False this settings is ignored. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.beet_settings import BeetSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BeetSettings from a JSON string
beet_settings_instance = BeetSettings.from_json(json)
# print the JSON string representation of the object
print(BeetSettings.to_json())

# convert the object into a dict
beet_settings_dict = beet_settings_instance.to_dict()
# create an instance of BeetSettings from a dict
beet_settings_from_dict = BeetSettings.from_dict(beet_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


