# Turbine

Models the location where the wind turbine is placed.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The turbine name. Should be unique within a wind farm. | 
**associated_wind_climate_id** | **str** | The id of the associated wind climate. | 
**turbine_model_id** | **str** | The unique id of the turbine model. | 
**is_installed** | **bool** | Whether the turbine is installed or not. | [optional] 
**production_yield** | **float** | The yield of the turbine. Units: MWh/year. | [optional] [default to 0]
**confidence_weighting** | **float** | The confidence weighting of rge ProductionYield. | [optional] [default to 0]
**location** | [**Location**](Location.md) | The location of the turbine. | 
**curtailment_rules** | [**List[TurbineManagementRule]**](TurbineManagementRule.md) | The turbine management rules for the turbine. | [optional] 
**park_wake_decay_constant** | **float** | Specifies the decay constant at the turbine, only defined when used in the Park calculation. | [optional] [default to 0.07]

## Example

```python
from dnv_windfarmer_client.models.turbine import Turbine

# TODO update the JSON string below
json = "{}"
# create an instance of Turbine from a JSON string
turbine_instance = Turbine.from_json(json)
# print the JSON string representation of the object
print(Turbine.to_json())

# convert the object into a dict
turbine_dict = turbine_instance.to_dict()
# create an instance of Turbine from a dict
turbine_from_dict = Turbine.from_dict(turbine_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


