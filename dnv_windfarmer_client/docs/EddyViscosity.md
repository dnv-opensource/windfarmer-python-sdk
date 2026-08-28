# EddyViscosity

The Eddy Viscosity wake model settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**use_large_wind_farm_model** | **bool** | Wether to to use the large wind farm model. Default: true | [optional] [default to True]
**large_wind_farm_correction_parameters** | [**LargeWindFarmCorrectionParameters**](LargeWindFarmCorrectionParameters.md) | The large wind farm correction parameter values. Can be omited if useLargeWindFarmModel is false. | [optional] 
**use_closely_spaced_turbines_wake_modification** | **bool** | If true, the calculation will apply the closely spaced turbine modifications to the wake model when appropriate The calculation only applies modifications wakes from turbines that are less than 3D apart. | [optional] [default to False]
**wake_profile_integration_method** | [**WakeProfileIntegrationMethod**](WakeProfileIntegrationMethod.md) | The method to use to combine multiple wakes when calculating the rotor averaged wind speed. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.eddy_viscosity import EddyViscosity

# TODO update the JSON string below
json = "{}"
# create an instance of EddyViscosity from a JSON string
eddy_viscosity_instance = EddyViscosity.from_json(json)
# print the JSON string representation of the object
print(EddyViscosity.to_json())

# convert the object into a dict
eddy_viscosity_dict = eddy_viscosity_instance.to_dict()
# create an instance of EddyViscosity from a dict
eddy_viscosity_from_dict = EddyViscosity.from_dict(eddy_viscosity_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


