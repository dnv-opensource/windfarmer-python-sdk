# ComprehensiveSiteClassification

Comprehensive site classification result with metadata and atmospheric conditions

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**metadata** | [**Metadata**](Metadata.md) | Metadata about the site and analysis parameters | [optional] 
**atmospheric_conditions** | [**AtmosphericConditions**](AtmosphericConditions.md) | Atmospheric condition data compatible with WindFarmer calculations | [optional] 

## Example

```python
from dnv_windfarmer_client.models.comprehensive_site_classification import ComprehensiveSiteClassification

# TODO update the JSON string below
json = "{}"
# create an instance of ComprehensiveSiteClassification from a JSON string
comprehensive_site_classification_instance = ComprehensiveSiteClassification.from_json(json)
# print the JSON string representation of the object
print(ComprehensiveSiteClassification.to_json())

# convert the object into a dict
comprehensive_site_classification_dict = comprehensive_site_classification_instance.to_dict()
# create an instance of ComprehensiveSiteClassification from a dict
comprehensive_site_classification_from_dict = ComprehensiveSiteClassification.from_dict(comprehensive_site_classification_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


