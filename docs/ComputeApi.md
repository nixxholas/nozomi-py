# swagger_client.ComputeApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**compute_all_index_get**](ComputeApi.md#compute_all_index_get) | **GET** /Compute/All/{index} | Obtains all of the relevant computes you own.
[**compute_get_guid_get**](ComputeApi.md#compute_get_guid_get) | **GET** /Compute/Get/{guid} | Obtains the specific compute.

# **compute_all_index_get**
> ComputeViewModelIEnumerablePaginatedViewModel compute_all_index_get(index)

Obtains all of the relevant computes you own.

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
api_instance = swagger_client.ComputeApi(swagger_client.ApiClient(configuration))
index = 56 # int | The 'page' of the list of results of every x items.

try:
    # Obtains all of the relevant computes you own.
    api_response = api_instance.compute_all_index_get(index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->compute_all_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| The &#x27;page&#x27; of the list of results of every x items. | 

### Return type

[**ComputeViewModelIEnumerablePaginatedViewModel**](ComputeViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **compute_get_guid_get**
> ComputeViewModel compute_get_guid_get(guid)

Obtains the specific compute.

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
api_instance = swagger_client.ComputeApi(swagger_client.ApiClient(configuration))
guid = 'guid_example' # str | The Guid of the compute in question.

try:
    # Obtains the specific compute.
    api_response = api_instance.compute_get_guid_get(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComputeApi->compute_get_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The Guid of the compute in question. | 

### Return type

[**ComputeViewModel**](ComputeViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

