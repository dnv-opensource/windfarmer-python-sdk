# dnv_windfarmer_client.AnnualEnergyProductionAsyncApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**annual_energy_production_async_delete**](AnnualEnergyProductionAsyncApi.md#annual_energy_production_async_delete) | **DELETE** /AnnualEnergyProductionAsync | Cancels the running of a calculation for the given Id.
[**annual_energy_production_async_get**](AnnualEnergyProductionAsyncApi.md#annual_energy_production_async_get) | **GET** /AnnualEnergyProductionAsync | Gets the status of an async AnnualEnergyProduction calculation.
[**annual_energy_production_async_post**](AnnualEnergyProductionAsyncApi.md#annual_energy_production_async_post) | **POST** /AnnualEnergyProductionAsync | Queues an energy calculation to be executed with the given inputs.


# **annual_energy_production_async_delete**
> annual_energy_production_async_delete(job_id=job_id)

Cancels the running of a calculation for the given Id.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import dnv_windfarmer_client
from dnv_windfarmer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dnv_windfarmer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = dnv_windfarmer_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dnv_windfarmer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dnv_windfarmer_client.AnnualEnergyProductionAsyncApi(api_client)
    job_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The ID of the calculation. (optional)

    try:
        # Cancels the running of a calculation for the given Id.
        api_instance.annual_energy_production_async_delete(job_id=job_id)
    except Exception as e:
        print("Exception when calling AnnualEnergyProductionAsyncApi->annual_energy_production_async_delete: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **UUID**| The ID of the calculation. | [optional] 

### Return type

void (empty response body)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status was queried successfully. |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **annual_energy_production_async_get**
> AnnualEnergyProductionJobStatus annual_energy_production_async_get(job_id=job_id)

Gets the status of an async AnnualEnergyProduction calculation.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import dnv_windfarmer_client
from dnv_windfarmer_client.models.annual_energy_production_job_status import AnnualEnergyProductionJobStatus
from dnv_windfarmer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dnv_windfarmer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = dnv_windfarmer_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dnv_windfarmer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dnv_windfarmer_client.AnnualEnergyProductionAsyncApi(api_client)
    job_id = UUID('38400000-8cf0-11bd-b23e-10b96e4ef00d') # UUID | The ID of the calculation. (optional)

    try:
        # Gets the status of an async AnnualEnergyProduction calculation.
        api_response = api_instance.annual_energy_production_async_get(job_id=job_id)
        print("The response of AnnualEnergyProductionAsyncApi->annual_energy_production_async_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnualEnergyProductionAsyncApi->annual_energy_production_async_get: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **job_id** | **UUID**| The ID of the calculation. | [optional] 

### Return type

[**AnnualEnergyProductionJobStatus**](AnnualEnergyProductionJobStatus.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | The status was queried successfully. |  -  |
**401** | Unauthorized |  -  |
**404** | No calculation exists with the given ID. |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **annual_energy_production_async_post**
> CalculationQueuedResult annual_energy_production_async_post(energy_calculation_inputs)

Queues an energy calculation to be executed with the given inputs.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import dnv_windfarmer_client
from dnv_windfarmer_client.models.calculation_queued_result import CalculationQueuedResult
from dnv_windfarmer_client.models.energy_calculation_inputs import EnergyCalculationInputs
from dnv_windfarmer_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to http://localhost
# See configuration.py for a list of all supported configuration parameters.
configuration = dnv_windfarmer_client.Configuration(
    host = "http://localhost"
)

# The client must configure the authentication and authorization parameters
# in accordance with the API server security policy.
# Examples for each auth method are provided below, use the example that
# satisfies your auth use case.

# Configure Bearer authorization (JWT): Bearer
configuration = dnv_windfarmer_client.Configuration(
    access_token = os.environ["BEARER_TOKEN"]
)

# Enter a context with an instance of the API client
with dnv_windfarmer_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = dnv_windfarmer_client.AnnualEnergyProductionAsyncApi(api_client)
    energy_calculation_inputs = dnv_windfarmer_client.EnergyCalculationInputs() # EnergyCalculationInputs | Energy efficiencies calculation inputs.

    try:
        # Queues an energy calculation to be executed with the given inputs.
        api_response = api_instance.annual_energy_production_async_post(energy_calculation_inputs)
        print("The response of AnnualEnergyProductionAsyncApi->annual_energy_production_async_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling AnnualEnergyProductionAsyncApi->annual_energy_production_async_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **energy_calculation_inputs** | [**EnergyCalculationInputs**](EnergyCalculationInputs.md)| Energy efficiencies calculation inputs. | 

### Return type

[**CalculationQueuedResult**](CalculationQueuedResult.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json, text/plain, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**202** | The calculation was queued successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

