# ReferenceAirDensity

The reference air density and elevation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**air_density_kg_per_m3** | **float** | The reference air density.  Units: kg/m3 | 
**lapse_rate_kg_per_m3_per_m** | **float** | The reference air density lapse rate.  Units: (kg/m3)/m | 
**elevation_m** | **float** | The elevation of the reference air density.  Units: m | 

## Example

```python
from dnv_windfarmer_client.models.reference_air_density import ReferenceAirDensity

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceAirDensity from a JSON string
reference_air_density_instance = ReferenceAirDensity.from_json(json)
# print the JSON string representation of the object
print(ReferenceAirDensity.to_json())

# convert the object into a dict
reference_air_density_dict = reference_air_density_instance.to_dict()
# create an instance of ReferenceAirDensity from a dict
reference_air_density_from_dict = ReferenceAirDensity.from_dict(reference_air_density_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


