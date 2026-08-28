# TurbineFlowAndPerformanceMatrixOutputSettings

The output settings for the turbine flow and performance matrices.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**output_mast_to_turbine_speed_up** | **bool** | If true the mast to turbine speedup will be output by the calculation. | [optional] [default to False]
**output_ambient_wind_speed** | **bool** | If true the Ambient Wind Speed with reference wind speeds at the mast flow and performance matrix will be output by the calculation. | [optional] [default to False]
**output_ambient_turbulence_intensity** | **bool** | If true the Ambient Turbulence Intensity with reference wind speeds at the mast flow and performance matrix will be output by the calculation. | [optional] [default to False]
**output_dominant_wake_center_line_wind_speed** | **bool** | If true the Dominant Wake Center-line Wind Speed with reference wind speeds at the mast flow and performance matrix will be output by the calculation. FPM is only available for wake models EddyViscosity and ModifiedPark. | [optional] [default to False]
**output_dominant_wake_offset** | **bool** | If true the Dominant Wake Offset with reference wind speeds at the mast flow and performance matrix will be output by the calculation. FPM is only available for wake models EddyViscosity and ModifiedPark. | [optional] [default to False]
**output_dominant_wake_width** | **bool** | If true the Dominant Wake Width with reference wind speeds at the mast flow and performance matrix will be output by the calculation. FPM is only available for wake model EddyViscosity. | [optional] [default to False]
**output_waked_wind_speed** | **bool** | If true the Waked Wind Speed with reference wind speeds at the mast flow and performance matrix will be output by the calculation. | [optional] [default to False]
**output_atmospheric_aware_waked_wind_speed** | **bool** | If true the Atmospheric Condition Aware Waked Wind Speed flow and performance matrix, with reference wind speeds at the mast, will be output by the calculation. FPM is only available for wake model CFD.ML v2.0 and later. | [optional] [default to False]
**output_waked_turbulence_intensity** | **bool** | If true the Waked Turbulence Intensity with reference wind speeds at the mast flow and performance matrix will be output by the calculation. | [optional] [default to False]
**output_power_output** | **bool** | If true the Power Output with reference wind speeds at the mast flow and performance matrix will be output by the calculation. | [optional] [default to False]
**output_atmospheric_aware_power_output** | **bool** | If true the Atmospheric Condition Aware Power Output with reference wind speeds at the mast flow and performance matrix will be output by the calculation. FPM is only available for wake model CFD.ML v2.0 and later. | [optional] [default to False]
**output_probability_distribution** | **bool** | If true the Probabilities distribution with reference wind speeds at the mast flow and performance matrix will be output by the calculation. | [optional] [default to False]
**output_upstream_turbine_causing_wake** | **bool** | If true the Upstream Turbine Name causing wake with reference wind speeds at the mast flow and performance matrix will be output by the calculation. FPM is only available for wake models EddyViscosity and ModifiedPark. | [optional] [default to False]
**output_operational_mode** | **bool** | If true the turbine operational mode for the turbine with reference wind speeds at the mast flow and performance matrix will be output | [optional] [default to False]
**local_turbine_wind_speeds_output_settings** | [**TurbineFlowAndPerformanceMatrixLocalWindSpeedsOutputSettings**](TurbineFlowAndPerformanceMatrixLocalWindSpeedsOutputSettings.md) | The output settings for the flow and performance matrices with local turbine wind speeds as reference. Only fill this property in json if matrices in local wind speeds are needed, otherwise omit the property. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.turbine_flow_and_performance_matrix_output_settings import TurbineFlowAndPerformanceMatrixOutputSettings

# TODO update the JSON string below
json = "{}"
# create an instance of TurbineFlowAndPerformanceMatrixOutputSettings from a JSON string
turbine_flow_and_performance_matrix_output_settings_instance = TurbineFlowAndPerformanceMatrixOutputSettings.from_json(json)
# print the JSON string representation of the object
print(TurbineFlowAndPerformanceMatrixOutputSettings.to_json())

# convert the object into a dict
turbine_flow_and_performance_matrix_output_settings_dict = turbine_flow_and_performance_matrix_output_settings_instance.to_dict()
# create an instance of TurbineFlowAndPerformanceMatrixOutputSettings from a dict
turbine_flow_and_performance_matrix_output_settings_from_dict = TurbineFlowAndPerformanceMatrixOutputSettings.from_dict(turbine_flow_and_performance_matrix_output_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


