# CfdmlTrainingSetAlignmentMetrics

The training set alignment metrics.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**edges_below_min_perc** | **float** | percent of gnn edge parameters in the call below the minimum encountered in the training set | [optional] 
**edges_above_max_perc** | **float** | percent of gnn edge parameters in the call above the maximum encountered in the training set | [optional] 
**vertices_below_min_perc** | **float** | percent of gnn vertex parameters in the call below the minimum encountered in the training set | [optional] 
**vertices_above_max_perc** | **float** | percent of gnn vertex parameters in the call above the maximum encountered in the training set | [optional] 

## Example

```python
from dnv_windfarmer_client.models.cfdml_training_set_alignment_metrics import CfdmlTrainingSetAlignmentMetrics

# TODO update the JSON string below
json = "{}"
# create an instance of CfdmlTrainingSetAlignmentMetrics from a JSON string
cfdml_training_set_alignment_metrics_instance = CfdmlTrainingSetAlignmentMetrics.from_json(json)
# print the JSON string representation of the object
print(CfdmlTrainingSetAlignmentMetrics.to_json())

# convert the object into a dict
cfdml_training_set_alignment_metrics_dict = cfdml_training_set_alignment_metrics_instance.to_dict()
# create an instance of CfdmlTrainingSetAlignmentMetrics from a dict
cfdml_training_set_alignment_metrics_from_dict = CfdmlTrainingSetAlignmentMetrics.from_dict(cfdml_training_set_alignment_metrics_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


