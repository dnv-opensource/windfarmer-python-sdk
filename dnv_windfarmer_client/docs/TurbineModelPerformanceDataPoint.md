# TurbineModelPerformanceDataPoint

Data for a single data point in the turbine model power curve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wind_speed_m_per_s** | **float** | The wind speed.  Units: m/s | 
**power_output_w** | **float** | The power output.  Units: W | 
**rotor_speed_radians_per_s** | **float** | The rotor speed.  Units: radians/s | 
**thrust_coefficient** | **float** | The thrust coefficient.  Units: - | 
**noise_difference_from_reference_curve_d_b** | **float** | The noise difference from the reference curve.  Units: dB | [optional] [default to 0]

## Example

```python
from dnv_windfarmer_client.models.turbine_model_performance_data_point import TurbineModelPerformanceDataPoint

# TODO update the JSON string below
json = "{}"
# create an instance of TurbineModelPerformanceDataPoint from a JSON string
turbine_model_performance_data_point_instance = TurbineModelPerformanceDataPoint.from_json(json)
# print the JSON string representation of the object
print(TurbineModelPerformanceDataPoint.to_json())

# convert the object into a dict
turbine_model_performance_data_point_dict = turbine_model_performance_data_point_instance.to_dict()
# create an instance of TurbineModelPerformanceDataPoint from a dict
turbine_model_performance_data_point_from_dict = TurbineModelPerformanceDataPoint.from_dict(turbine_model_performance_data_point_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


