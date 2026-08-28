# Status

Status response model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**message** | **str** | Gets or sets the response message. | 
**wind_farmer_services_api_version** | **str** | Gets or sets the WindFarmer services API assembly version. | 
**calculation_library_version** | **str** | Gets or sets the calculation library version. | 

## Example

```python
from dnv_windfarmer_client.models.status import Status

# TODO update the JSON string below
json = "{}"
# create an instance of Status from a JSON string
status_instance = Status.from_json(json)
# print the JSON string representation of the object
print(Status.to_json())

# convert the object into a dict
status_dict = status_instance.to_dict()
# create an instance of Status from a dict
status_from_dict = Status.from_dict(status_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


