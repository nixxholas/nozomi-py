# swagger_client.RequestApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**request_all_get**](RequestApi.md#request_all_get) | **GET** /Request/All | Retrieves all requests owned by the stated user with a pagination of 100 items.
[**request_create_post**](RequestApi.md#request_create_post) | **POST** /Request/Create | Create a request.
[**request_delete_guid_delete**](RequestApi.md#request_delete_guid_delete) | **DELETE** /Request/Delete/{guid} | Delete a request.
[**request_get_guid_get**](RequestApi.md#request_get_guid_get) | **GET** /Request/Get/{guid} | Retrieves the request with the mentioned guid.
[**request_update_put**](RequestApi.md#request_update_put) | **PUT** /Request/Update | Update a request.

# **request_all_get**
> RequestViewModelIEnumerablePaginatedViewModel request_all_get(index=index)

Retrieves all requests owned by the stated user with a pagination of 100 items.

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
api_instance = swagger_client.RequestApi(swagger_client.ApiClient(configuration))
index = 0 # int | The 'page' of the request list you're viewing (optional) (default to 0)

try:
    # Retrieves all requests owned by the stated user with a pagination of 100 items.
    api_response = api_instance.request_all_get(index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestApi->request_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| The &#x27;page&#x27; of the request list you&#x27;re viewing | [optional] [default to 0]

### Return type

[**RequestViewModelIEnumerablePaginatedViewModel**](RequestViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_create_post**
> str request_create_post(body=body)

Create a request.

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
api_instance = swagger_client.RequestApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateRequestInputModel() # CreateRequestInputModel | The supposed properties/parameters of the request. (optional)

try:
    # Create a request.
    api_response = api_instance.request_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestApi->request_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateRequestInputModel**](CreateRequestInputModel.md)| The supposed properties/parameters of the request. | [optional] 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_delete_guid_delete**
> str request_delete_guid_delete(guid)

Delete a request.

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
api_instance = swagger_client.RequestApi(swagger_client.ApiClient(configuration))
guid = 'guid_example' # str | The unique ID of the request.

try:
    # Delete a request.
    api_response = api_instance.request_delete_guid_delete(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestApi->request_delete_guid_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The unique ID of the request. | 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_get_guid_get**
> RequestViewModel request_get_guid_get(guid)

Retrieves the request with the mentioned guid.

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
api_instance = swagger_client.RequestApi(swagger_client.ApiClient(configuration))
guid = 'guid_example' # str | Guid of the request

try:
    # Retrieves the request with the mentioned guid.
    api_response = api_instance.request_get_guid_get(guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestApi->request_get_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| Guid of the request | 

### Return type

[**RequestViewModel**](RequestViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **request_update_put**
> str request_update_put(body=body)

Update a request.

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
api_instance = swagger_client.RequestApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateRequestInputModel() # UpdateRequestInputModel | The supposed properties/parameters of the request. (optional)

try:
    # Update a request.
    api_response = api_instance.request_update_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling RequestApi->request_update_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateRequestInputModel**](UpdateRequestInputModel.md)| The supposed properties/parameters of the request. | [optional] 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

