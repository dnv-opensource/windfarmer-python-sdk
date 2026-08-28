# FlowModel

The flow model data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**reference_directions_degrees** | **List[float]** | The reference wind directions for each of the speedups provided. A sorted array is expected. | 
**speeds_ups** | [**List[SpeedUpsForLocation]**](SpeedUpsForLocation.md) | The relative speedups at each location. | 

## Example

```python
from dnv_windfarmer_client.models.flow_model import FlowModel

# TODO update the JSON string below
json = "{}"
# create an instance of FlowModel from a JSON string
flow_model_instance = FlowModel.from_json(json)
# print the JSON string representation of the object
print(FlowModel.to_json())

# convert the object into a dict
flow_model_dict = flow_model_instance.to_dict()
# create an instance of FlowModel from a dict
flow_model_from_dict = FlowModel.from_dict(flow_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


