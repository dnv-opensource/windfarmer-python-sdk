# TurbineFlowAndPerformanceMatrixLocalWindSpeedsOutputSettings

The output settings for flow and performance matrices in local turbine wind speeds

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_power_output** | **bool** | If true the Power Output with reference wind speeds at the mast flow and performance matrix will be output by the calculation. | [optional] [default to False]
**output_waked_wind_speed** | **bool** | If true the Waked Wind Speed with reference wind speeds at the mast flow and performance matrix will be output by the calculation. | [optional] [default to False]
**output_probability_distribution** | **bool** | If true the Probabilities distribution with local turbine wind speeds flow and performance matrix will be output by the calculation. | [optional] [default to False]
**output_waked_turbulence_intensity** | **bool** | If true the Waked Turbulence Intensity with local turbine wind speeds flow and performance matrix will be output by the calculation. | [optional] [default to False]
**output_ambient_turbulence_intensity** | **bool** | If true the Ambient Turbulence Intensity with local turbine wind speeds flow and performance matrix will be output by the calculation. | [optional] [default to False]
**output_operational_mode** | **bool** | If true the Operation model with local turbine wind speeds flow and performance matrix will be output by the calculation. | [optional] [default to False]

## Example

```python
from dnv_windfarmer_client.models.turbine_flow_and_performance_matrix_local_wind_speeds_output_settings import TurbineFlowAndPerformanceMatrixLocalWindSpeedsOutputSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TurbineFlowAndPerformanceMatrixLocalWindSpeedsOutputSettings from a JSON string
turbine_flow_and_performance_matrix_local_wind_speeds_output_settings_instance = TurbineFlowAndPerformanceMatrixLocalWindSpeedsOutputSettings.from_json(json)
# print the JSON string representation of the object
print(TurbineFlowAndPerformanceMatrixLocalWindSpeedsOutputSettings.to_json())

# convert the object into a dict
turbine_flow_and_performance_matrix_local_wind_speeds_output_settings_dict = turbine_flow_and_performance_matrix_local_wind_speeds_output_settings_instance.to_dict()
# create an instance of TurbineFlowAndPerformanceMatrixLocalWindSpeedsOutputSettings from a dict
turbine_flow_and_performance_matrix_local_wind_speeds_output_settings_from_dict = TurbineFlowAndPerformanceMatrixLocalWindSpeedsOutputSettings.from_dict(turbine_flow_and_performance_matrix_local_wind_speeds_output_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


