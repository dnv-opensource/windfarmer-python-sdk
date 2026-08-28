# WeightedCfdmlIntermediateData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**intermediate_cfdml_v2_data** | **Dict[str, Dict[str, Dict[str, List[TurbineBlockageEfficiency]]]]** | The per-flowcase, per-turbine blockage efficiencies for the CFDML V2 model. | [optional] 
**intermediate_cfdml_v1_data** | **Dict[str, Dict[str, List[TurbineBlockageEfficiency]]]** | The per-flowcase, per-turbine blockage efficiencies for the CFDML V1 model. | [optional] 
**training_set_alignment_metrics** | [**CfdmlTrainingSetAlignmentMetrics**](CfdmlTrainingSetAlignmentMetrics.md) | The training set alignment metrics. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.weighted_cfdml_intermediate_data import WeightedCfdmlIntermediateData

# TODO update the JSON string below
json = "{}"
# create an instance of WeightedCfdmlIntermediateData from a JSON string
weighted_cfdml_intermediate_data_instance = WeightedCfdmlIntermediateData.from_json(json)
# print the JSON string representation of the object
print(WeightedCfdmlIntermediateData.to_json())

# convert the object into a dict
weighted_cfdml_intermediate_data_dict = weighted_cfdml_intermediate_data_instance.to_dict()
# create an instance of WeightedCfdmlIntermediateData from a dict
weighted_cfdml_intermediate_data_from_dict = WeightedCfdmlIntermediateData.from_dict(weighted_cfdml_intermediate_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


