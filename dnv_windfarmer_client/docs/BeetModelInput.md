# BeetModelInput

Input model used for the calculation, includes turbine locations and performance curve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**turbines** | [**List[TurbineLocation]**](TurbineLocation.md) | Details of the turbines on the wind farm. | [optional] 
**turbine_performance** | [**List[TurbinePerformance]**](TurbinePerformance.md) | A list of turbine performance characteristics at different wind speeds. | [optional] 
**significant_atmospheric_stability** | **bool** | Specifies whether there is significant atmospheric stability (true), or if the atmosphere is predominantly neutral or unstable (false). | [optional] 

## Example

```python
from dnv_windfarmer_client.models.beet_model_input import BeetModelInput

# TODO update the JSON string below
json = "{}"
# create an instance of BeetModelInput from a JSON string
beet_model_input_instance = BeetModelInput.from_json(json)
# print the JSON string representation of the object
print(BeetModelInput.to_json())

# convert the object into a dict
beet_model_input_dict = beet_model_input_instance.to_dict()
# create an instance of BeetModelInput from a dict
beet_model_input_from_dict = BeetModelInput.from_dict(beet_model_input_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


