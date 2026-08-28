# TurbineFlowAndPerformanceMatrix

The turbine flow and performance matrix data for one turbine.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**turbine_name** | **str** | The turbine name. | [optional] 
**wind_farm_name** | **str** | The wind farm name. | [optional] 
**direction_for_first_bin_centre_degrees** | **float** | The direction of the first direction bin. Units: degrees | [optional] 
**bin_center_wind_speeds_at_mast_m_per_s** | **List[float]** | The bin center wind speeds at the associated mast. Units: m/s | [optional] 
**ambient_wind_speed_m_per_s** | **List[List[float]]** | Outer List is direction sectors. Inner List is turbine ambient wind speed at each mast wind speed. Units: m/s | [optional] 
**ambient_turbulence_intensity_percentage** | **List[List[float]]** | Outer List is direction sectors. Inner List is turbine ambient wind speed at each mast wind speed. Units: percent | [optional] 
**dominant_wake_center_line_wind_speed_m_per_s** | **List[List[float]]** | Outer List is direction sectors. Inner List is dominant wake center-line wind speed at each mast wind speed. | [optional] 
**dominant_wake_width** | **List[List[float]]** | Outer List is direction sectors. Inner List is dominant wake width at each mast wind speed. | [optional] 
**dominant_wake_offset_m** | **List[List[float]]** | Outer List is direction sectors. Inner List is dominant wake offset at each mast wind speed. Units: m | [optional] 
**waked_wind_speed_m_per_s** | **List[List[float]]** | Outer List is direction sectors. Inner List is wake adjusted wind speed at each mast wind speed. Units: m/s | [optional] 
**atmospheric_condition_aware_waked_wind_speed_m_per_s** | **Dict[str, List[List[float]]]** | Dict keys are atmosphericConditionClassIds Outer List is direction sectors. Inner List is wake adjusted wind speed at each mast wind speed for the given atmospheric condition class. Units: m/s | [optional] 
**waked_turbulence_intensity_percentage** | **List[List[float]]** | Outer List is direction sectors. Inner List is wake adjusted turbulence intensity at each mast wind speed. Units: percent | [optional] 
**spot_power_output_w** | **List[List[float]]** | Outer List is direction sectors. Inner List is turbine power output at each mast wind speed. Units: W | [optional] 
**atmospheric_condition_aware_spot_power_output_w** | **Dict[str, List[object]]** | Dict keys are atmosphericConditionClassIds Outer List is direction sectors. Inner List is turbine power output at each mast wind speed for the given atmospheric condition class. Units: W | [optional] 
**bin_power_output_w** | **List[List[float]]** | Outer List is direction sectors. Inner List is turbine power output representative of the wind speed bin. Units: W | [optional] 
**probability_distribution** | **List[List[float]]** | Outer List is the direction sectors. Inner List is the turbine probability distribution at each mast wind speed. | [optional] 
**upstream_turbine_causing_wake** | **List[List[str]]** | Outer list is direction sectors. Inner list is the name of the upstream turbine that causes the wake. | [optional] 
**turbine_operational_mode** | **List[List[str]]** | Outer list is direction sectors. Inner list is the turbine active mode at each mast wind speed. | [optional] 
**mast_to_turbine_speed_up** | **List[float]** | Gets or sets the mast to turbine speed up. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.turbine_flow_and_performance_matrix import TurbineFlowAndPerformanceMatrix

# TODO update the JSON string below
json = "{}"
# create an instance of TurbineFlowAndPerformanceMatrix from a JSON string
turbine_flow_and_performance_matrix_instance = TurbineFlowAndPerformanceMatrix.from_json(json)
# print the JSON string representation of the object
print(TurbineFlowAndPerformanceMatrix.to_json())

# convert the object into a dict
turbine_flow_and_performance_matrix_dict = turbine_flow_and_performance_matrix_instance.to_dict()
# create an instance of TurbineFlowAndPerformanceMatrix from a dict
turbine_flow_and_performance_matrix_from_dict = TurbineFlowAndPerformanceMatrix.from_dict(turbine_flow_and_performance_matrix_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


