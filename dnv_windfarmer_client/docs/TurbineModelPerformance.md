# TurbineModelPerformance

Defines a turbine model power curve for a specific mode, air density etc.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**turbine_operational_mode** | **str** | The turbine mode, defaults to normal. | [default to 'normal']
**adjusted_high_speed_cut_out_m_per_s** | **float** | The high wind speed cut out, adjusted to model the hysteresis effect.  Units: m/s | 
**adjusted_low_speed_cut_in_m_per_s** | **float** | The low speed cut in, adjusted to model the hysteresis effect. Units: m/s | 
**low_speed_cut_in_m_per_s** | **float** | The low wind speed cut in.  Units: m/s | 
**high_speed_cut_out_m_per_s** | **float** | The high wind speed cut out.  Units: m/s | 
**turbulence_intensity** | **float** | The turbulence intensity. Meta data only, not used in calculations Units: percent | [optional] 
**air_density_kg_per_m3** | **float** | The air density.  Units: kg/m3 | 
**temperature_deg_c** | **float** | The temperature.  Units: Deg C | [optional] 
**yaw_misalignment_degrees** | **float** | The yaw misalignment.  Units: degrees | [optional] 
**power_derating_delta_k_w** | **float** | The power derating delta.  Units: kW | [optional] 
**performance_data_points** | [**List[TurbineModelPerformanceDataPoint]**](TurbineModelPerformanceDataPoint.md) | The performance specific data. | 

## Example

```python
from dnv_windfarmer_client.models.turbine_model_performance import TurbineModelPerformance

# TODO update the JSON string below
json = "{}"
# create an instance of TurbineModelPerformance from a JSON string
turbine_model_performance_instance = TurbineModelPerformance.from_json(json)
# print the JSON string representation of the object
print(TurbineModelPerformance.to_json())

# convert the object into a dict
turbine_model_performance_dict = turbine_model_performance_instance.to_dict()
# create an instance of TurbineModelPerformance from a dict
turbine_model_performance_from_dict = TurbineModelPerformance.from_dict(turbine_model_performance_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


