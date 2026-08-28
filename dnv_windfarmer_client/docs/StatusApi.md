# dnv_windfarmer_client.StatusApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**status_get**](StatusApi.md#status_get) | **GET** /Status | Checks the status of the API and validates authentication.


# **status_get**
> Status status_get()

Checks the status of the API and validates authentication.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import dnv_windfarmer_client
from dnv_windfarmer_client.models.status import Status
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
    api_instance = dnv_windfarmer_client.StatusApi(api_client)

    try:
        # Checks the status of the API and validates authentication.
        api_response = api_instance.status_get()
        print("The response of StatusApi->status_get:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling StatusApi->status_get: %s\n" % e)
```



### Parameters

This endpoint does not need any parameter.

### Return type

[**Status**](Status.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Returns Ok for successful status check. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

