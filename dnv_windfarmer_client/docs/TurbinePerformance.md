# TurbinePerformance

Performance data for turbine.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wind_speed_m_per_s** | **float** | The wind speed. Units: m/s | [optional] 
**power_output_k_w** | **float** | The power output. Units: kilo watts | [optional] 
**thrust_coefficient** | **float** | The thrust coefficient. | [optional] 
**frequency_pc** | **float** | The probability of this wind speed occurring. Units: %. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.turbine_performance import TurbinePerformance

# TODO update the JSON string below
json = "{}"
# create an instance of TurbinePerformance from a JSON string
turbine_performance_instance = TurbinePerformance.from_json(json)
# print the JSON string representation of the object
print(TurbinePerformance.to_json())

# convert the object into a dict
turbine_performance_dict = turbine_performance_instance.to_dict()
# create an instance of TurbinePerformance from a dict
turbine_performance_from_dict = TurbinePerformance.from_dict(turbine_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


