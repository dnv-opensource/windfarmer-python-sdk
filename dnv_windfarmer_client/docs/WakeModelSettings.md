# WakeModelSettings

The wake model settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wake_model_type** | [**WakeModelType**](WakeModelType.md) | Wake model to use. If NoWakeModel the gross power will be provided. | [optional] 
**eddy_viscosity** | [**EddyViscosity**](EddyViscosity.md) | The Eddy Viscosity wake model settings. Can be omited if WakeModelType is not EddyViscosity. | [optional] 
**modified_park** | [**ModifiedPark**](ModifiedPark.md) | The Modified Park wake model settings. Can be omited if WakeModelType is not ModifiedPark. | [optional] 
**turb_o_park** | [**TurbOPark**](TurbOPark.md) | The TurbOPark wake model settings.  Can be omited if WakeModelType is not TurbOPark. | [optional] 
**cfdml** | [**Cfdml**](Cfdml.md) | The CFD.ML wake model settings. Can be omited if WakeModelType is not CFDML. | [optional] 
**no_wake_model** | [**NoWakeModel**](NoWakeModel.md) | No Wake model settings. Can be omited if WakeModelType is not NoWakeModel. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.wake_model_settings import WakeModelSettings

# TODO update the JSON string below
json = "{}"
# create an instance of WakeModelSettings from a JSON string
wake_model_settings_instance = WakeModelSettings.from_json(json)
# print the JSON string representation of the object
print(WakeModelSettings.to_json())

# convert the object into a dict
wake_model_settings_dict = wake_model_settings_instance.to_dict()
# create an instance of WakeModelSettings from a dict
wake_model_settings_from_dict = WakeModelSettings.from_dict(wake_model_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


