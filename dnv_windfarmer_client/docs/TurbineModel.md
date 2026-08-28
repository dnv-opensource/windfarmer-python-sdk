# TurbineModel

Model data for a particular Turbine model.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | The unique id of the turbine model. | 
**rotor_diameter_m** | **float** | The diameter of the turbine rotor.  Units: m | 
**number_of_blades** | **int** | The number of blades. Units: - | 
**hub_height_m** | **float** | The height of the hub above the turbine base.  Units: m | 
**performance_data** | [**List[TurbineModelPerformance]**](TurbineModelPerformance.md) | The performance specific data. | 
**power_control** | [**PowerControlType**](PowerControlType.md) | The power control type of the turbine. | 
**wind_speed_class** | [**WindSpeedClass**](WindSpeedClass.md) | Wind speed class as per IEC edition 3 standard - &#39;1&#39;, &#39;2&#39;, &#39;3&#39;. | [optional] 
**turbulence_intensity_class** | [**TurbulenceIntensityClass**](TurbulenceIntensityClass.md) | Turbulence intensity class as per IEC edition 3 standard - &#39;A&#39;, &#39;B&#39;, &#39;C&#39;. | [optional] 
**reference_noise_level** | **float** | Reference noise level for this turbine. dB TODO this is a dummy really - need a whole noise DTO here including octave bands etc. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.turbine_model import TurbineModel

# TODO update the JSON string below
json = "{}"
# create an instance of TurbineModel from a JSON string
turbine_model_instance = TurbineModel.from_json(json)
# print the JSON string representation of the object
print(TurbineModel.to_json())

# convert the object into a dict
turbine_model_dict = turbine_model_instance.to_dict()
# create an instance of TurbineModel from a dict
turbine_model_from_dict = TurbineModel.from_dict(turbine_model_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


