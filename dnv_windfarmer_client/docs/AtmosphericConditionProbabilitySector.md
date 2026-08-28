# AtmosphericConditionProbabilitySector

An atmospheric condition probability distribution sector.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**from_direction_degrees** | **float** | Applies to flow cases with directions from and including direction. | 
**to_direction_degrees** | **float** | Applies to flow cases with directions up to (excluding) direction. | 
**atmospheric_condition_class_ids** | **List[str]** | The order of atmospheric condition class IDs in the ProbabilityForClass list. | 
**probability_for_classes** | **List[float]** | The probability for each of the specified AtmosphericConditionClassIds.  1.0 &#x3D; 100% probability for the corresponding class.  The probabilities for a class are normalised to sum to 1.0 within this sector | 

## Example

```python
from dnv_windfarmer_client.models.atmospheric_condition_probability_sector import AtmosphericConditionProbabilitySector

# TODO update the JSON string below
json = "{}"
# create an instance of AtmosphericConditionProbabilitySector from a JSON string
atmospheric_condition_probability_sector_instance = AtmosphericConditionProbabilitySector.from_json(json)
# print the JSON string representation of the object
print(AtmosphericConditionProbabilitySector.to_json())

# convert the object into a dict
atmospheric_condition_probability_sector_dict = atmospheric_condition_probability_sector_instance.to_dict()
# create an instance of AtmosphericConditionProbabilitySector from a dict
atmospheric_condition_probability_sector_from_dict = AtmosphericConditionProbabilitySector.from_dict(atmospheric_condition_probability_sector_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


