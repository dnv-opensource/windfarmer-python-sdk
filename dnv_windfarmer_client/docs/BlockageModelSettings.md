# BlockageModelSettings

The blockage model settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockage_model_type** | [**BlockageModelType**](BlockageModelType.md) | The blockage model to use. | [optional] 
**beet** | [**BeetSettings**](BeetSettings.md) | DNV BEET model settings. Can be omitted if BlockageModelType is not BEET. | [optional] 
**cfdml** | [**CfdmlBlockageSettings**](CfdmlBlockageSettings.md) | DNV CFD.ML model settings. Can be omitted if BlockageModelType is not CFD.ML. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.blockage_model_settings import BlockageModelSettings

# TODO update the JSON string below
json = "{}"
# create an instance of BlockageModelSettings from a JSON string
blockage_model_settings_instance = BlockageModelSettings.from_json(json)
# print the JSON string representation of the object
print(BlockageModelSettings.to_json())

# convert the object into a dict
blockage_model_settings_dict = blockage_model_settings_instance.to_dict()
# create an instance of BlockageModelSettings from a dict
blockage_model_settings_from_dict = BlockageModelSettings.from_dict(blockage_model_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


