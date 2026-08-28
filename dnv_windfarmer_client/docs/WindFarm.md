# WindFarm

The data relating to one wind farm, mainly the collection of turbines in that wind farm.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**name** | **str** | The name of the wind farm. | 
**turbines** | [**List[Turbine]**](Turbine.md) | The collection of turbines in the wind farm. | 
**is_neighbor** | **bool** | Specifies whether the wind farm should be considered a neighboring wind farm and therefore not included in the total energy yield. | 
**include_in_blockage_calculation** | **bool** | Whether this wind farm should be included in the blockage calculation or not. | 

## Example

```python
from dnv_windfarmer_client.models.wind_farm import WindFarm

# TODO update the JSON string below
json = "{}"
# create an instance of WindFarm from a JSON string
wind_farm_instance = WindFarm.from_json(json)
# print the JSON string representation of the object
print(WindFarm.to_json())

# convert the object into a dict
wind_farm_dict = wind_farm_instance.to_dict()
# create an instance of WindFarm from a dict
wind_farm_from_dict = WindFarm.from_dict(wind_farm_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


