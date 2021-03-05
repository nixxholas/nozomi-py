# swagger_client.ComponentTypeApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**component_type_all_get**](ComponentTypeApi.md#component_type_all_get) | **GET** /ComponentType/All | Obtain all of the component types that are publicly available or the ones that you own.

# **component_type_all_get**
> ComponentTypeViewModelIEnumerablePaginatedViewModel component_type_all_get(index=index)

Obtain all of the component types that are publicly available or the ones that you own.

### Example
```python
from __future__ import print_function
import time
import swagger_client
from swagger_client.rest import ApiException
from pprint import pprint

# Configure API key authorization: API Key
configuration = swagger_client.Configuration()
configuration.api_key['X-Api-Key'] = 'YOUR_API_KEY'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['X-Api-Key'] = 'Bearer'

# create an instance of the API class
api_instance = swagger_client.ComponentTypeApi(swagger_client.ApiClient(configuration))
index = 0 # int | the 'page' of the list of results in 50s. (optional) (default to 0)

try:
    # Obtain all of the component types that are publicly available or the ones that you own.
    api_response = api_instance.component_type_all_get(index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentTypeApi->component_type_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| the &#x27;page&#x27; of the list of results in 50s. | [optional] [default to 0]

### Return type

[**ComponentTypeViewModelIEnumerablePaginatedViewModel**](ComponentTypeViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

