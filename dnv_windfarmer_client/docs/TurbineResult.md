# TurbineResult

The results, from an Energy Calculation, associated with one turbine

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**turbine_name** | **str** | The turbine name. | [optional] 
**turbine_location** | [**Location**](Location.md) | The turbine location. | [optional] 
**wind_farm_name** | **str** | The wind farm name. | [optional] 
**ideal_annual_yield_mwh_per_year** | **float** | A reference yield that represents a theoretical production where the turbine is located at the location of its initiation mast. Units: MWh/yr | [optional] 
**gross_annual_yield_mwh_per_year** | **float** | The energy output assuming no wake losses, no cut-out hysteresis and no curtailment. Units: MWh/yr | [optional] 
**internal_blockage_on_annual_yield_mwh_per_year** | **float** | The energy output including internal blockage efficiency, only different to BlockageOn variant for CFDML as a wake calculation. | [optional] 
**blockage_on_annual_yield_mwh_per_year** | **float** | The energy output including blockage efficiency, but with no internal wakes, no large wind farm correction, no cut-out hysteresis and no curtailment. Units: MWh/yr | [optional] 
**internal_wakes_on_annual_yield_mwh_per_year** | **float** | The energy output including wake losses from this wind farm only, but with no large wind farm correction, no cut-out hysteresis and no curtailment. Units: MWh/yr | [optional] 
**hysteresis_adjustment_on_annual_yield_mwh_per_year** | **float** | The energy output including wake losses from this wind farm only and cut-out hysteresis but no large wind farm correction and no curtailment. Units: MWh/yr | [optional] 
**large_wind_farm_correction_on_annual_yield_mwh_per_year** | **float** | The energy output including wake losses from this wind farm only and cut-out hysteresis and including large wind farm correction but not curtailment. Units: MWh/yr | [optional] 
**neighbors_wakes_on_annual_yield_mwh_per_year** | **float** | The energy output including wake losses from this and neighboring wind farms, and cut-out hysteresis, and including large wind farm correction but not curtailment. Units: MWh/yr | [optional] 
**full_annual_yield_mwh_per_year** | **float** | The energy output from the full model, included all known effects. Units: MWh/yr | [optional] 
**tuning_annual_yield_mwh_per_year** | **float** | The energy output from the full model, included effects selected in the tuning process. Units: MWh/yr | [optional] 
**mean_turbulence_intensity** | **Dict[str, float]** | Mean turbulence intensity for each variant | [optional] 
**free_mean_wind_speed_m_per_s** | **float** | The free stream mean wind speed, excluding any wake effects. Units: m/s | [optional] 
**full_mean_wind_speed_m_per_s** | **float** | The mean wind speed including wake effects from the full model. Units: m/s | [optional] 
**ambient_mean_turbulence_intensity_percentage** | **float** | The mean ambient turbulence intensity, excludes any wake effects. Units: percent | [optional] 
**full_mean_turbulence_intensity_percentage** | **float** | The mean turbulence intensity, including all known effects. Units: percent | [optional] 
**air_density_at_hub_height_kg_per_m3** | **float** | Air density at turbine hub height.  Units: kg/m3 | [optional] 
**used_performance_table_ids** | **List[str]** | A list of the performance data table ids (mode@air density) used by the calculation. Shutdown has been filtered out | [optional] 

## Example

```python
from dnv_windfarmer_client.models.turbine_result import TurbineResult

# TODO update the JSON string below
json = "{}"
# create an instance of TurbineResult from a JSON string
turbine_result_instance = TurbineResult.from_json(json)
# print the JSON string representation of the object
print(TurbineResult.to_json())

# convert the object into a dict
turbine_result_dict = turbine_result_instance.to_dict()
# create an instance of TurbineResult from a dict
turbine_result_from_dict = TurbineResult.from_dict(turbine_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


