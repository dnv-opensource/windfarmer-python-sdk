# WindClimate

Data describing the wind climate at a particular elevation at a measurement location.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id for the wind climate, typically the mast name plus the height above ground. Needs to be the same as property AssociatedWindClimateId in Turbine | 
**location** | [**Location**](Location.md) | The wind climate location: easting, northing and base height | 
**height_above_ground_m** | **float** | The wind climate height above ground. Units: m | 
**number_of_direction_sectors** | **int** | The number of directions for which there is climate data.  Units: - | 
**direction_for_first_bin_centre_degrees** | **float** | The wind direction of the first climate data point. Units: degrees | 
**wind_speed_bin_upper_limits_m_per_s** | **List[float]** | The upper limit for each wind speed bin. It is assumed that the lower limit for each bin is the upper limit of the preceding bin, except for the first bin which is assumed to start at zero. Units: m/s | 
**probability_distribution** | **List[List[float]]** | Outer List is direction sectors Inner List is probabilities at each wind speed. | 
**turbulence_intensity** | **List[List[float]]** | Outer List is direction sectors Inner List is turbulence intensity at each wind speed TI &#x3D; std deviation of wind speed / mean wind speed Note: This is a ratio not a percent. | 

## Example

```python
from dnv_windfarmer_client.models.wind_climate import WindClimate

# TODO update the JSON string below
json = "{}"
# create an instance of WindClimate from a JSON string
wind_climate_instance = WindClimate.from_json(json)
# print the JSON string representation of the object
print(WindClimate.to_json())

# convert the object into a dict
wind_climate_dict = wind_climate_instance.to_dict()
# create an instance of WindClimate from a dict
wind_climate_from_dict = WindClimate.from_dict(wind_climate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


