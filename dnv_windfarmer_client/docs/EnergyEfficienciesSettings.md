# EnergyEfficienciesSettings

The Annual Energy Production (AEP) calculation settings.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**calculate_efficiencies** | **bool** | If true, the energy calculation will be run several times so that the efficiencies can be calculated. | 
**calculate_ideal_yield** | **bool** | If true, the ideal (reference) yield is calculated. | [optional] [default to False]
**calculate_sensitivity_curve** | **bool** | If true, wind speed perturbation to energy perturbation sensitivity curves are computed and returned in the results. | [optional] [default to False]
**include_hysteresis_effect** | **bool** | If true, the high wind cut-out hysteresis effect will be included. | 
**include_curtailment_rules** | **bool** | If true, the turbine management rules will be applied. | 
**turbine_flow_and_performance_matrix_output_settings** | [**TurbineFlowAndPerformanceMatrixOutputSettings**](TurbineFlowAndPerformanceMatrixOutputSettings.md) | The output settings for the turbine flow and performance matrices. | 
**number_of_direction_sectors_for_wake_calculation** | **int** | The number of direction sectors to use for the wake calculation. Units: - | 
**maximum_wind_speed_for_evaluation_m_per_s** | **float** | If this is non-zero then all flow cases up to this mast wind speed will be evaluated and reported If this is zero, then flow cases will be evaluated for every wind-speed bin that has non-zero frequency of occurrence. Units: m/s | 
**extrapolation_ambient_turbulence** | [**ExtrapolationAmbientTurbulence**](ExtrapolationAmbientTurbulence.md) | The setting which defines whether to assume a constant std. dev. of wind speed or rather const. turbulence intensity. | [optional] 
**air_density_correction_method** | [**AirDensityCorrectionMethod**](AirDensityCorrectionMethod.md) | The method to use to extrapolate the power curve to the turbine location air density. | [optional] 
**wake_model** | [**WakeModelSettings**](WakeModelSettings.md) | The wake model settings. | 
**blockage_model** | [**BlockageModelSettings**](BlockageModelSettings.md) | The blockage model settings | 

## Example

```python
from dnv_windfarmer_client.models.energy_efficiencies_settings import EnergyEfficienciesSettings

# TODO update the JSON string below
json = "{}"
# create an instance of EnergyEfficienciesSettings from a JSON string
energy_efficiencies_settings_instance = EnergyEfficienciesSettings.from_json(json)
# print the JSON string representation of the object
print(EnergyEfficienciesSettings.to_json())

# convert the object into a dict
energy_efficiencies_settings_dict = energy_efficiencies_settings_instance.to_dict()
# create an instance of EnergyEfficienciesSettings from a dict
energy_efficiencies_settings_from_dict = EnergyEfficienciesSettings.from_dict(energy_efficiencies_settings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


