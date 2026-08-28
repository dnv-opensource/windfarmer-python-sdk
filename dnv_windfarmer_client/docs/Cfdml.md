# Cfdml

The CFD.ML wake model settings

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**gnn_type** | [**GnnType**](GnnType.md) | The GNN type to use in CFD.ML predictions | [optional] 
**gnn_version** | **str** | Version of the gnn to use. See release notes for the version number supported. | [optional] [default to '1.1']
**extrapolation_model** | [**CfdmlWindSpeedExtrapolationModel**](CfdmlWindSpeedExtrapolationModel.md) | Model used to extrapolate Cfdml v2 single wind speed model.  Only relevant when defining Cfdml as a wake model. Ignored when defining Cfdml as a blockage model only. Required for Version &amp;gt;&#x3D; 2.0 | [optional] 

## Example

```python
from dnv_windfarmer_client.models.cfdml import Cfdml

# TODO update the JSON string below
json = "{}"
# create an instance of Cfdml from a JSON string
cfdml_instance = Cfdml.from_json(json)
# print the JSON string representation of the object
print(Cfdml.to_json())

# convert the object into a dict
cfdml_dict = cfdml_instance.to_dict()
# create an instance of Cfdml from a dict
cfdml_from_dict = Cfdml.from_dict(cfdml_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


