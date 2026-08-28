# ModifiedPark

The Modified Park wake model settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_large_wind_farm_model** | **bool** | Wether to to use the large wind farm model. Default: true | [optional] [default to True]
**large_wind_farm_correction_parameters** | [**LargeWindFarmCorrectionParameters**](LargeWindFarmCorrectionParameters.md) | The large wind farm correction parameter values. Can be omited if useLargeWindFarmModel is false. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.modified_park import ModifiedPark

# TODO update the JSON string below
json = "{}"
# create an instance of ModifiedPark from a JSON string
modified_park_instance = ModifiedPark.from_json(json)
# print the JSON string representation of the object
print(ModifiedPark.to_json())

# convert the object into a dict
modified_park_dict = modified_park_instance.to_dict()
# create an instance of ModifiedPark from a dict
modified_park_from_dict = ModifiedPark.from_dict(modified_park_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


