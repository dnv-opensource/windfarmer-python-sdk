# TurbineManagementRule

Data for one turbine management rule The rule is that the turbine will be in active mode when the different conditions are met

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wind_direction_from** | **float** | The minimum wind direction that the rule applies to. | [optional] 
**wind_direction_to** | **float** | The maximum wind direction that the rule applies to. | [optional] 
**minimum_wind_speed_m_per_s** | **float** | The minimum wind speed that the rule applies to. | [optional] 
**maximum_wind_speed_m_per_s** | **float** | The maximum wind speed that the rule applies to. | [optional] 
**time_from_as_time_of_day** | **str** | The start time of a daily time range specified as an absolute time of day. | [optional] 
**time_to_as_time_of_day** | **str** | The end time of daily time range specified as an absolute time of day. | [optional] 
**time_from_as_sun_rise_offset** | **str** | The start time of a daily time range specified as an offset from sunrise. A +ve offset means after sunrise while a -ve means before sunrise. | [optional] 
**time_to_as_sun_rise_offset** | **str** | The end time of a daily time range specified as an offset from sunrise. A +ve offset means after sunrise while a -ve means before sunrise. | [optional] 
**time_from_as_sun_set_offset** | **str** | The start time of a daily time range specified as an offset from sunset. A +ve offset means after sunset while a -ve means before sunset. | [optional] 
**time_to_as_sun_set_offset** | **str** | The end time of a daily time range specified as offset from sunset. A +ve offset means after sunset while a -ve means before sunset. | [optional] 
**start_day_of_year** | **int** | The start day of year that the rule applies to, inclusive. Assumes non leap year. | [optional] 
**end_day_of_year** | **int** | The end day of year that the rule applies to, inclusive. Assumes non leap year. Note: if day 59 (28th of Feb) is specified, the calculation will interpret this as till the end of February which means that if a time series has records on the 29th of Feb these be included in this interval. | [optional] 
**minimum_temperature_degrees_celsius** | **float** | The minimum temperature that the rule applies to in celsius. | [optional] 
**maximum_temperature_degrees_celsius** | **float** | The maximum temperature that the rule applies to in celsius. | [optional] 
**active_mode** | **str** | Active mode for the turbine. If shutdown, value should be \&quot;ShutDown\&quot;. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.turbine_management_rule import TurbineManagementRule

# TODO update the JSON string below
json = "{}"
# create an instance of TurbineManagementRule from a JSON string
turbine_management_rule_instance = TurbineManagementRule.from_json(json)
# print the JSON string representation of the object
print(TurbineManagementRule.to_json())

# convert the object into a dict
turbine_management_rule_dict = turbine_management_rule_instance.to_dict()
# create an instance of TurbineManagementRule from a dict
turbine_management_rule_from_dict = TurbineManagementRule.from_dict(turbine_management_rule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


