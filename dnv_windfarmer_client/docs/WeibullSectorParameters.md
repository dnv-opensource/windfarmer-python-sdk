# WeibullSectorParameters

The weibull parameters for a direction sector

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**a** | **float** | The Weibull scale parameter | 
**k** | **float** | The Weibull shape parameter | 
**probability** | **float** | This direction sector probability.  Expect that all sector probabilities add up to 1.0 | 

## Example

```python
from dnv_windfarmer_client.models.weibull_sector_parameters import WeibullSectorParameters

# TODO update the JSON string below
json = "{}"
# create an instance of WeibullSectorParameters from a JSON string
weibull_sector_parameters_instance = WeibullSectorParameters.from_json(json)
# print the JSON string representation of the object
print(WeibullSectorParameters.to_json())

# convert the object into a dict
weibull_sector_parameters_dict = weibull_sector_parameters_instance.to_dict()
# create an instance of WeibullSectorParameters from a dict
weibull_sector_parameters_from_dict = WeibullSectorParameters.from_dict(weibull_sector_parameters_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


