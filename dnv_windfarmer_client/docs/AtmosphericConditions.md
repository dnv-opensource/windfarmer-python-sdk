# AtmosphericConditions

Contains the atmospheric condition information to enrich existing wind climates

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**atmospheric_condition_classes** | [**List[AtmosphericConditionClass]**](AtmosphericConditionClass.md) | A list of atmospheric condition classes. | 
**atmospheric_condition_probability_distribution** | [**List[AtmosphericConditionProbabilitySector]**](AtmosphericConditionProbabilitySector.md) | Probability distribution describing by direction frequency of the atmospheric condition classes. | 

## Example

```python
from dnv_windfarmer_client.models.atmospheric_conditions import AtmosphericConditions

# TODO update the JSON string below
json = "{}"
# create an instance of AtmosphericConditions from a JSON string
atmospheric_conditions_instance = AtmosphericConditions.from_json(json)
# print the JSON string representation of the object
print(AtmosphericConditions.to_json())

# convert the object into a dict
atmospheric_conditions_dict = atmospheric_conditions_instance.to_dict()
# create an instance of AtmosphericConditions from a dict
atmospheric_conditions_from_dict = AtmosphericConditions.from_dict(atmospheric_conditions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


