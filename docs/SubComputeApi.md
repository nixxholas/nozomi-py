# swagger_client.SubComputeApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**sub_compute_all_by_child_child_compute_guid_get**](SubComputeApi.md#sub_compute_all_by_child_child_compute_guid_get) | **GET** /SubCompute/AllByChild/{childComputeGuid} | Obtains all of the relevant parent computes the child compute has.
[**sub_compute_all_by_parent_parent_compute_guid_get**](SubComputeApi.md#sub_compute_all_by_parent_parent_compute_guid_get) | **GET** /SubCompute/AllByParent/{parentComputeGuid} | Obtains all of the relevant child computes the parent compute has.
[**sub_compute_all_index_get**](SubComputeApi.md#sub_compute_all_index_get) | **GET** /SubCompute/All/{index} | Obtains all of the relevant Sub Computes you own.
[**sub_compute_get_get**](SubComputeApi.md#sub_compute_get_get) | **GET** /SubCompute/Get | Obtains the specific sub compute.

# **sub_compute_all_by_child_child_compute_guid_get**
> ComputeViewModelIEnumerablePaginatedViewModel sub_compute_all_by_child_child_compute_guid_get(child_compute_guid, index=index)

Obtains all of the relevant parent computes the child compute has.

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
api_instance = swagger_client.SubComputeApi(swagger_client.ApiClient(configuration))
child_compute_guid = 'child_compute_guid_example' # str | The child compute that has these computes as its parent.
index = 0 # int | The 'page' of the list of results of every x items. (optional) (default to 0)

try:
    # Obtains all of the relevant parent computes the child compute has.
    api_response = api_instance.sub_compute_all_by_child_child_compute_guid_get(child_compute_guid, index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubComputeApi->sub_compute_all_by_child_child_compute_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **child_compute_guid** | **str**| The child compute that has these computes as its parent. | 
 **index** | **int**| The &#x27;page&#x27; of the list of results of every x items. | [optional] [default to 0]

### Return type

[**ComputeViewModelIEnumerablePaginatedViewModel**](ComputeViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_compute_all_by_parent_parent_compute_guid_get**
> ComputeViewModelIEnumerablePaginatedViewModel sub_compute_all_by_parent_parent_compute_guid_get(parent_compute_guid, index=index)

Obtains all of the relevant child computes the parent compute has.

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
api_instance = swagger_client.SubComputeApi(swagger_client.ApiClient(configuration))
parent_compute_guid = 'parent_compute_guid_example' # str | The parent compute that has these computes as its child.
index = 0 # int | The 'page' of the list of results of every x items. (optional) (default to 0)

try:
    # Obtains all of the relevant child computes the parent compute has.
    api_response = api_instance.sub_compute_all_by_parent_parent_compute_guid_get(parent_compute_guid, index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubComputeApi->sub_compute_all_by_parent_parent_compute_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_compute_guid** | **str**| The parent compute that has these computes as its child. | 
 **index** | **int**| The &#x27;page&#x27; of the list of results of every x items. | [optional] [default to 0]

### Return type

[**ComputeViewModelIEnumerablePaginatedViewModel**](ComputeViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_compute_all_index_get**
> SubComputeViewModelIEnumerablePaginatedViewModel sub_compute_all_index_get(index)

Obtains all of the relevant Sub Computes you own.

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
api_instance = swagger_client.SubComputeApi(swagger_client.ApiClient(configuration))
index = 56 # int | The 'page' of the list of results of every x items.

try:
    # Obtains all of the relevant Sub Computes you own.
    api_response = api_instance.sub_compute_all_index_get(index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubComputeApi->sub_compute_all_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| The &#x27;page&#x27; of the list of results of every x items. | 

### Return type

[**SubComputeViewModelIEnumerablePaginatedViewModel**](SubComputeViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **sub_compute_get_get**
> SubComputeViewModel sub_compute_get_get(parent_compute_guid=parent_compute_guid, child_compute_guid=child_compute_guid)

Obtains the specific sub compute.

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
api_instance = swagger_client.SubComputeApi(swagger_client.ApiClient(configuration))
parent_compute_guid = 'parent_compute_guid_example' # str | The parent compute key. (optional)
child_compute_guid = 'child_compute_guid_example' # str | The child compute key. (optional)

try:
    # Obtains the specific sub compute.
    api_response = api_instance.sub_compute_get_get(parent_compute_guid=parent_compute_guid, child_compute_guid=child_compute_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling SubComputeApi->sub_compute_get_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **parent_compute_guid** | **str**| The parent compute key. | [optional] 
 **child_compute_guid** | **str**| The child compute key. | [optional] 

### Return type

[**SubComputeViewModel**](SubComputeViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

