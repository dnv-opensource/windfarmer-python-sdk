# BlockageModelIntermediateData

Blockage model intermediate data output

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intermediate_data** | [**WeightedBeetIntermediateData**](WeightedBeetIntermediateData.md) | The optional intermediate result data. | [optional] 
**intermediate_cfdml_v2_data** | [**WeightedCfdmlIntermediateData**](WeightedCfdmlIntermediateData.md) | The per-flowcase, per-turbine blockage efficiencies for the CFDML V2 model. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.blockage_model_intermediate_data import BlockageModelIntermediateData

# TODO update the JSON string below
json = "{}"
# create an instance of BlockageModelIntermediateData from a JSON string
blockage_model_intermediate_data_instance = BlockageModelIntermediateData.from_json(json)
# print the JSON string representation of the object
print(BlockageModelIntermediateData.to_json())

# convert the object into a dict
blockage_model_intermediate_data_dict = blockage_model_intermediate_data_instance.to_dict()
# create an instance of BlockageModelIntermediateData from a dict
blockage_model_intermediate_data_from_dict = BlockageModelIntermediateData.from_dict(blockage_model_intermediate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


