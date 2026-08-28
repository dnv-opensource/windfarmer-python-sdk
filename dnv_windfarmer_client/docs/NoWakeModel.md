# NoWakeModel

No wake model option settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_large_wind_farm_model** | **bool** | Wether to to use the large wind farm model. Default: true | [optional] [default to True]
**large_wind_farm_correction_parameters** | [**LargeWindFarmCorrectionParameters**](LargeWindFarmCorrectionParameters.md) | The large wind farm correction parameter values. Can be omited if useLargeWindFarmModel is false. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.no_wake_model import NoWakeModel

# TODO update the JSON string below
json = "{}"
# create an instance of NoWakeModel from a JSON string
no_wake_model_instance = NoWakeModel.from_json(json)
# print the JSON string representation of the object
print(NoWakeModel.to_json())

# convert the object into a dict
no_wake_model_dict = no_wake_model_instance.to_dict()
# create an instance of NoWakeModel from a dict
no_wake_model_from_dict = NoWakeModel.from_dict(no_wake_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


