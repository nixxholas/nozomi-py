# swagger_client.RequestPropertyApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_property_all_by_request_get**](RequestPropertyApi.md#request_property_all_by_request_get) | **GET** /RequestProperty/AllByRequest | Obtain all analysed components you have created, relative to that specific request.
[**request_property_all_get**](RequestPropertyApi.md#request_property_all_get) | **GET** /RequestProperty/All | Obtain all request properties you have created/own.
[**request_property_create_post**](RequestPropertyApi.md#request_property_create_post) | **POST** /RequestProperty/Create | Create a request property.
[**request_property_delete_guid_delete**](RequestPropertyApi.md#request_property_delete_guid_delete) | **DELETE** /RequestProperty/Delete/{guid} | Delete a request property
[**request_property_update_put**](RequestPropertyApi.md#request_property_update_put) | **PUT** /RequestProperty/Update | Update a request property.

# **request_property_all_by_request_get**
> RequestPropertyViewModelIEnumerablePaginatedViewModel request_property_all_by_request_get(request_guid=request_guid, index=index)

Obtain all analysed components you have created, relative to that specific request.

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
api_instance = swagger_client.RequestPropertyApi(swagger_client.ApiClient(configuration))
request_guid = 'request_guid_example' # str | The request guid you are referring to. (optional)
index = 0 # int | The 'page' of the list of results in 100s. (optional) (default to 0)

try:
    # Obtain all analysed components you have created, relative to that specific request.
    api_response = api_instance.request_property_all_by_request_get(request_guid=request_guid, index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestPropertyApi->request_property_all_by_request_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_guid** | **str**| The request guid you are referring to. | [optional] 
 **index** | **int**| The &#x27;page&#x27; of the list of results in 100s. | [optional] [default to 0]

### Return type

[**RequestPropertyViewModelIEnumerablePaginatedViewModel**](RequestPropertyViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_property_all_get**
> RequestPropertyViewModelIEnumerablePaginatedViewModel request_property_all_get(index=index)

Obtain all request properties you have created/own.

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
api_instance = swagger_client.RequestPropertyApi(swagger_client.ApiClient(configuration))
index = 0 # int | The 'page' of the list of results in 100s. (optional) (default to 0)

try:
    # Obtain all request properties you have created/own.
    api_response = api_instance.request_property_all_get(index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestPropertyApi->request_property_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| The &#x27;page&#x27; of the list of results in 100s. | [optional] [default to 0]

### Return type

[**RequestPropertyViewModelIEnumerablePaginatedViewModel**](RequestPropertyViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_property_create_post**
> str request_property_create_post(body=body)

Create a request property.

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
api_instance = swagger_client.RequestPropertyApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRequestPropertyInputModel() # CreateRequestPropertyInputModel | The supposed properties/parameters of the request property. (optional)

try:
    # Create a request property.
    api_response = api_instance.request_property_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestPropertyApi->request_property_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRequestPropertyInputModel**](CreateRequestPropertyInputModel.md)| The supposed properties/parameters of the request property. | [optional] 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_property_delete_guid_delete**
> str request_property_delete_guid_delete(guid)

Delete a request property

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
api_instance = swagger_client.RequestPropertyApi(swagger_client.ApiClient(configuration))
guid = 'guid_example' # str | The unique identifier of the deletion attempt.

try:
    # Delete a request property
    api_response = api_instance.request_property_delete_guid_delete(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestPropertyApi->request_property_delete_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The unique identifier of the deletion attempt. | 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_property_update_put**
> str request_property_update_put(body=body)

Update a request property.

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
api_instance = swagger_client.RequestPropertyApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateRequestPropertyInputModel() # UpdateRequestPropertyInputModel | The supposed properties/parameters of the request property. (optional)

try:
    # Update a request property.
    api_response = api_instance.request_property_update_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestPropertyApi->request_property_update_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRequestPropertyInputModel**](UpdateRequestPropertyInputModel.md)| The supposed properties/parameters of the request property. | [optional] 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

