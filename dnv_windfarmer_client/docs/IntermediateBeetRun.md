# IntermediateBeetRun

A class to hold an intermediate blockage run.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**blockage_input** | [**BeetModelInput**](BeetModelInput.md) | Gets or sets the blockage model input. | [optional] 
**turbine_model_name** | **str** | The turbine model name. | [optional] 
**hub_height** | **float** | The turbine model hub height | [optional] 
**average_air_density_at_hub_height** | **float** | The average air density at hub height. | [optional] 
**wind_climate_name** | **str** | The wind climate name. | [optional] 
**average_adjusted_free_stream_mean_wind_speed** | **float** | The average adjusted free stream mean wind speed. | [optional] 
**weighted_result** | **float** | The weighted result. | [optional] 
**blockage_effect** | **float** | The blockage effect. | [optional] 
**density_rotor_diameters** | **float** | Gets the density rotor diameters (Internal use only). | [optional] 
**blockage_loss_ws** | **float** | Gets the blockage loss wind speed percentage (Internal use only). | [optional] 
**hub_height_rotor_diameter_multiplier** | **float** | Gets the hub height rotor diameter multiplier (Internal use only). | [optional] 

## Example

```python
from dnv_windfarmer_client.models.intermediate_beet_run import IntermediateBeetRun

# TODO update the JSON string below
json = "{}"
# create an instance of IntermediateBeetRun from a JSON string
intermediate_beet_run_instance = IntermediateBeetRun.from_json(json)
# print the JSON string representation of the object
print(IntermediateBeetRun.to_json())

# convert the object into a dict
intermediate_beet_run_dict = intermediate_beet_run_instance.to_dict()
# create an instance of IntermediateBeetRun from a dict
intermediate_beet_run_from_dict = IntermediateBeetRun.from_dict(intermediate_beet_run_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


