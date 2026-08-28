# dnv_windfarmer_client.BlockageCorrectionApi

All URIs are relative to *http://localhost*

Method | HTTP request | Description
------------- | ------------- | -------------
[**blockage_correction_post**](BlockageCorrectionApi.md#blockage_correction_post) | **POST** /BlockageCorrection | Gets the blockage correction result for the given inputs.


# **blockage_correction_post**
> BeetModelOutput blockage_correction_post(beet_model_input)

Gets the blockage correction result for the given inputs.

### Example

* Bearer (JWT) Authentication (Bearer):

```python
import dnv_windfarmer_client
from dnv_windfarmer_client.models.beet_model_input import BeetModelInput
from dnv_windfarmer_client.models.beet_model_output import BeetModelOutput
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
    api_instance = dnv_windfarmer_client.BlockageCorrectionApi(api_client)
    beet_model_input = dnv_windfarmer_client.BeetModelInput() # BeetModelInput | The blockage model calculation inputs.

    try:
        # Gets the blockage correction result for the given inputs.
        api_response = api_instance.blockage_correction_post(beet_model_input)
        print("The response of BlockageCorrectionApi->blockage_correction_post:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling BlockageCorrectionApi->blockage_correction_post: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **beet_model_input** | [**BeetModelInput**](BeetModelInput.md)| The blockage model calculation inputs. | 

### Return type

[**BeetModelOutput**](BeetModelOutput.md)

### Authorization

[Bearer](../README.md#Bearer)

### HTTP request headers

 - **Content-Type**: application/json-patch+json, application/json, text/json, application/*+json
 - **Accept**: application/json, text/plain, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Calculation results were retrieved successfully. |  -  |
**400** | Bad request. |  -  |
**401** | Unauthorized |  -  |
**500** | Internal server error. |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

