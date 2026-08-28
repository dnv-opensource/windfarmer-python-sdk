# WeightedBeetIntermediateData

The weighted blockage model intermediate result data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wind_farm_name** | **List[str]** | Gets or sets the used windFarms. | [optional] 
**intermediate_blockage_run** | [**List[IntermediateBeetRun]**](IntermediateBeetRun.md) | An intermediate blockage run. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.weighted_beet_intermediate_data import WeightedBeetIntermediateData

# TODO update the JSON string below
json = "{}"
# create an instance of WeightedBeetIntermediateData from a JSON string
weighted_beet_intermediate_data_instance = WeightedBeetIntermediateData.from_json(json)
# print the JSON string representation of the object
print(WeightedBeetIntermediateData.to_json())

# convert the object into a dict
weighted_beet_intermediate_data_dict = weighted_beet_intermediate_data_instance.to_dict()
# create an instance of WeightedBeetIntermediateData from a dict
weighted_beet_intermediate_data_from_dict = WeightedBeetIntermediateData.from_dict(weighted_beet_intermediate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


