# EnergyCalculationInputs

A class for holding all the calculation inputs required for the energy calculation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**project_info** | [**ProjectInfo**](ProjectInfo.md) | Project information. | 
**wind_farms** | [**List[WindFarm]**](WindFarm.md) | Wind farms to be included in the analysis. | 
**turbine_models** | [**List[TurbineModel]**](TurbineModel.md) | Turbine models used in the wind farms. | 
**wind_climates** | [**List[WindClimate]**](WindClimate.md) | The wind climate data provided as frequency and turbulence distributions. For use when this measured data exists. If this list is specified then the List&amp;lt;WeibullWindClimate&amp;gt; EnergyCalculationInputs.WeibullWindClimates list should not be specified. | [optional] 
**weibull_wind_climates** | [**List[WeibullWindClimate]**](WeibullWindClimate.md) | The wind climate data provided as weibull parameters for probabilities and a single turbulence value. For use when measured data is not available. If this list is specified then the List&amp;lt;WindClimate&amp;gt; EnergyCalculationInputs.WindClimates list should not be specified. | [optional] 
**atmospheric_conditions** | [**AtmosphericConditions**](AtmosphericConditions.md) | The atmospheric conditions that apply to existing wind climates. | [optional] 
**reference_air_density** | [**ReferenceAirDensity**](ReferenceAirDensity.md) | The reference air density for the wind farm. | 
**flow_model** | [**FlowModel**](FlowModel.md) | The flow model data. | 
**energy_efficiencies_settings** | [**EnergyEfficienciesSettings**](EnergyEfficienciesSettings.md) | The calculation settings. | 

## Example

```python
from dnv_windfarmer_client.models.energy_calculation_inputs import EnergyCalculationInputs

# TODO update the JSON string below
json = "{}"
# create an instance of EnergyCalculationInputs from a JSON string
energy_calculation_inputs_instance = EnergyCalculationInputs.from_json(json)
# print the JSON string representation of the object
print(EnergyCalculationInputs.to_json())

# convert the object into a dict
energy_calculation_inputs_dict = energy_calculation_inputs_instance.to_dict()
# create an instance of EnergyCalculationInputs from a dict
energy_calculation_inputs_from_dict = EnergyCalculationInputs.from_dict(energy_calculation_inputs_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


