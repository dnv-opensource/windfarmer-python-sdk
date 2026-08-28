# CalculationQueuedResult

Represents the result of queuing a job in OneCompute.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**job_id** | **UUID** | Gets the Job ID. | [optional] 

## Example

```python
from dnv_windfarmer_client.models.calculation_queued_result import CalculationQueuedResult

# TODO update the JSON string below
json = "{}"
# create an instance of CalculationQueuedResult from a JSON string
calculation_queued_result_instance = CalculationQueuedResult.from_json(json)
# print the JSON string representation of the object
print(CalculationQueuedResult.to_json())

# convert the object into a dict
calculation_queued_result_dict = calculation_queued_result_instance.to_dict()
# create an instance of CalculationQueuedResult from a dict
calculation_queued_result_from_dict = CalculationQueuedResult.from_dict(calculation_queued_result_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)


