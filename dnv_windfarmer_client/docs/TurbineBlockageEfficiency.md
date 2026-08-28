# TurbineBlockageEfficiency

A turbine blockage efficiency result

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**turbine_name** | **str** | Turbine name | 
**blockage_efficiency** | **float** | Turbine blockage efficiency | 

## Example

```python
from dnv_windfarmer_client.models.turbine_blockage_efficiency import TurbineBlockageEfficiency

# TODO update the JSON string below
json = "{}"
# create an instance of TurbineBlockageEfficiency from a JSON string
turbine_blockage_efficiency_instance = TurbineBlockageEfficiency.from_json(json)
# print the JSON string representation of the object
print(TurbineBlockageEfficiency.to_json())

# convert the object into a dict
turbine_blockage_efficiency_dict = turbine_blockage_efficiency_instance.to_dict()
# create an instance of TurbineBlockageEfficiency from a dict
turbine_blockage_efficiency_from_dict = TurbineBlockageEfficiency.from_dict(turbine_blockage_efficiency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


