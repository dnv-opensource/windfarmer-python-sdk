# WindFarmAepOutput

Annual energy production results for a wind farm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**wind_farm_name** | **str** | The wind farm name. | [optional] 
**gross_annual_energy_yield_mwh_per_year** | **float** | The energy output assuming no blockage, no wake losses, no cut-out hysteresis and no curtailment. Units: MWh/yr | [optional] 
**ideal_annual_energy_yield_mwh_per_year** | **float** | The ideal energy yield. Units : MWh/yr | [optional] 
**internal_blockage_on_annual_energy_yield_mwh_per_year** | **float** | The energy output including internal blockage efficiency, only different to BlockageOn variant for CFDML as a wake calculation. | [optional] 
**blockage_on_annual_energy_yield_mwh_per_year** | **float** | The energy output assuming no wake losses, no cut-out hysteresis and no curtailment. Units: MWh/yr | [optional] 
**internal_wakes_on_annual_energy_yield_mwh_per_year** | **float** | The energy output including wake losses from this wind farm only, but with no large wind farm correction, no cut-out hysteresis and no curtailment. Units: MWh/yr | [optional] 
**hysteresis_adjustment_on_annual_energy_yield_mwh_per_year** | **float** | The energy output including wake losses from this wind farm only and cut-out hysteresis but no large wind farm correction and no curtailment. Units: MWh/yr | [optional] 
**large_wind_farm_correction_on_annual_energy_yield_mwh_per_year** | **float** | The energy output including wake losses from this wind farm only and cut-out hysteresis and including large wind farm correction but not curtailment. Units: MWh/yr | [optional] 
**neighbors_wakes_on_annual_energy_yield_mwh_per_year** | **float** | The energy output including wake losses from this and neighboring wind farms, and cut-out hysteresis, and including large wind farm correction but not curtailment. Units: MWh/yr | [optional] 
**full_annual_energy_yield_mwh_per_year** | **float** | The full anuual energy yield. Units: MWh/yr | [optional] 
**turbine_results** | [**List[TurbineResult]**](TurbineResult.md) | Turbines on the wind farm. | [optional] 
**turbine_flow_and_performance_matrices_with_mast_binning** | [**List[TurbineFlowAndPerformanceMatrix]**](TurbineFlowAndPerformanceMatrix.md) | Flow and performance matrix data with mast reference wind speeds. | [optional] 
**turbine_flow_and_performance_matrices_with_turbine_binning** | [**List[TurbineFlowAndPerformanceMatrix]**](TurbineFlowAndPerformanceMatrix.md) | Flow and performance matrix data with turbine local wind speeds. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.wind_farm_aep_output import WindFarmAepOutput

# TODO update the JSON string below
json = "{}"
# create an instance of WindFarmAepOutput from a JSON string
wind_farm_aep_output_instance = WindFarmAepOutput.from_json(json)
# print the JSON string representation of the object
print(WindFarmAepOutput.to_json())

# convert the object into a dict
wind_farm_aep_output_dict = wind_farm_aep_output_instance.to_dict()
# create an instance of WindFarmAepOutput from a dict
wind_farm_aep_output_from_dict = WindFarmAepOutput.from_dict(wind_farm_aep_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


