# TurbOPark

The TurbOPark wake model settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wake_expansion** | **float** | Parameter A : wake expansion calibration parameter. | [optional] [default to 0.04]

## Example

```python
from dnv_windfarmer_client.models.turb_o_park import TurbOPark

# TODO update the JSON string below
json = "{}"
# create an instance of TurbOPark from a JSON string
turb_o_park_instance = TurbOPark.from_json(json)
# print the JSON string representation of the object
print(TurbOPark.to_json())

# convert the object into a dict
turb_o_park_dict = turb_o_park_instance.to_dict()
# create an instance of TurbOPark from a dict
turb_o_park_from_dict = TurbOPark.from_dict(turb_o_park_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


