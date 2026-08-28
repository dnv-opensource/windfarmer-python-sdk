# BeetModelOutput

The blockage model outputs

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockage_effect** | **float** | The blockage factor | [optional] 
**density_rotor_diameters** | **float** | Gets the density rotor diameters (Internal use only). | [optional] 
**blockage_loss_ws** | **float** | Gets the blockage loss wind speed percentage (Internal use only). | [optional] 
**hub_height_rotor_diameter_multiplier** | **float** | Gets the hub height rotor diameter multiplier (Internal use only). | [optional] 

## Example

```python
from dnv_windfarmer_client.models.beet_model_output import BeetModelOutput

# TODO update the JSON string below
json = "{}"
# create an instance of BeetModelOutput from a JSON string
beet_model_output_instance = BeetModelOutput.from_json(json)
# print the JSON string representation of the object
print(BeetModelOutput.to_json())

# convert the object into a dict
beet_model_output_dict = beet_model_output_instance.to_dict()
# create an instance of BeetModelOutput from a dict
beet_model_output_from_dict = BeetModelOutput.from_dict(beet_model_output_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


