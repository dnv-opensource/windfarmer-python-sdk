# WeibullWindClimate

Weibull parameters describing the wind climate at a particular height and location

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Unique id for the wind climate, typically the mast/turbine name plus the height above ground. Needs to be the same as property AssociatedWindClimateId in Turbine | 
**location** | [**Location**](Location.md) | The wind climate location: easting, northing and base height | 
**height_above_ground_m** | **float** | The wind climate height above ground. Units: m | 
**number_of_direction_sectors** | **int** | The number of directions for which there is climate data.  Units: - | 
**direction_for_first_bin_centre_degrees** | **float** | The wind direction of the first climate data point. Units: degrees | 
**sector_weibull_parameters** | [**List[WeibullSectorParameters]**](WeibullSectorParameters.md) | Weibull parameters for each sector. Length of list must be int WeibullWindClimate.NumberOfDirectionSectors and first element corresponds to direction double WeibullWindClimate.DirectionForFirstBinCentre Sum of all sectors probabilities should be 1. | 
**turbulence_intensity** | **float** | A flat turbulence intensity value. Units: ratio Note: This is a ratio not a percent. | 

## Example

```python
from dnv_windfarmer_client.models.weibull_wind_climate import WeibullWindClimate

# TODO update the JSON string below
json = "{}"
# create an instance of WeibullWindClimate from a JSON string
weibull_wind_climate_instance = WeibullWindClimate.from_json(json)
# print the JSON string representation of the object
print(WeibullWindClimate.to_json())

# convert the object into a dict
weibull_wind_climate_dict = weibull_wind_climate_instance.to_dict()
# create an instance of WeibullWindClimate from a dict
weibull_wind_climate_from_dict = WeibullWindClimate.from_dict(weibull_wind_climate_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


