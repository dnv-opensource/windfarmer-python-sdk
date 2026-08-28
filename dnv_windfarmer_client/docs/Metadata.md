# Metadata

Metadata about the site classification analysis

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**site_latitude** | **float** | Latitude of the site | [optional] 
**site_longitude** | **float** | Longitude of the site | [optional] 
**nearest_era5_grid_latitude** | **float** | Latitude of the nearest Era5 grid point | [optional] 
**nearest_era5_grid_longitude** | **float** | Longitude of the nearest Era5 grid point | [optional] 
**distance_to_nearest_grid_point_km** | **float** | Distance to the nearest Era5 grid point in kilometers | [optional] 
**number_of_sectors** | **int** | Number of directional sectors used in the analysis | [optional] 
**coastline_detection_radius_km** | **float** | Radius in kilometers used for coastline detection | [optional] 
**stability_classification_method** | **str** | Method used for stability classification (e.g., \&quot;hf\&quot;, \&quot;mol\&quot;, \&quot;blend\&quot;) | [optional] 
**era5_time_series_start_date** | **str** | Start date of the Era5 time series data | [optional] 
**era5_time_series_end_date** | **str** | End date of the Era5 time series data | [optional] 

## Example

```python
from dnv_windfarmer_client.models.metadata import Metadata

# TODO update the JSON string below
json = "{}"
# create an instance of Metadata from a JSON string
metadata_instance = Metadata.from_json(json)
# print the JSON string representation of the object
print(Metadata.to_json())

# convert the object into a dict
metadata_dict = metadata_instance.to_dict()
# create an instance of Metadata from a dict
metadata_from_dict = Metadata.from_dict(metadata_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


