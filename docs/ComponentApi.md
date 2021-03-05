# swagger_client.ComponentApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**component_all_get**](ComponentApi.md#component_all_get) | **GET** /Component/All | Obtain all components you have created.
[**component_create_post**](ComponentApi.md#component_create_post) | **POST** /Component/Create | Create a component.
[**component_delete_delete**](ComponentApi.md#component_delete_delete) | **DELETE** /Component/Delete | Delete a component.
[**component_get_guid_get**](ComponentApi.md#component_get_guid_get) | **GET** /Component/Get/{guid} | Obtain the component and its historical values.
[**component_update_put**](ComponentApi.md#component_update_put) | **PUT** /Component/Update | Update a component.

# **component_all_get**
> ComponentViewModelIEnumerablePaginatedViewModel component_all_get(request_guid=request_guid, index=index)

Obtain all components you have created.

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
api_instance = swagger_client.ComponentApi(swagger_client.ApiClient(configuration))
request_guid = 'request_guid_example' # str | The unique identifier of the request that contains this component. (optional)
index = 0 # int | The 'page' of the list of results in 100s (optional) (default to 0)

try:
    # Obtain all components you have created.
    api_response = api_instance.component_all_get(request_guid=request_guid, index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentApi->component_all_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **request_guid** | **str**| The unique identifier of the request that contains this component. | [optional] 
 **index** | **int**| The &#x27;page&#x27; of the list of results in 100s | [optional] [default to 0]

### Return type

[**ComponentViewModelIEnumerablePaginatedViewModel**](ComponentViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **component_create_post**
> str component_create_post(body=body)

Create a component.

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
api_instance = swagger_client.ComponentApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateComponentInputModel() # CreateComponentInputModel | The supposed properties/parameters of the component. (optional)

try:
    # Create a component.
    api_response = api_instance.component_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentApi->component_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateComponentInputModel**](CreateComponentInputModel.md)| The supposed properties/parameters of the component. | [optional] 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **component_delete_delete**
> str component_delete_delete(guid=guid)

Delete a component.

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
api_instance = swagger_client.ComponentApi(swagger_client.ApiClient(configuration))
guid = 'guid_example' # str | The unique identifier of the component to delete. (optional)

try:
    # Delete a component.
    api_response = api_instance.component_delete_delete(guid=guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentApi->component_delete_delete: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The unique identifier of the component to delete. | [optional] 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **component_get_guid_get**
> ComponentViewModel component_get_guid_get(guid, index=index)

Obtain the component and its historical values.

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
api_instance = swagger_client.ComponentApi(swagger_client.ApiClient(configuration))
guid = 'guid_example' # str | The unique identifier of the component.
index = 0 # int | The 'page' of the list of historical values in 100s (optional) (default to 0)

try:
    # Obtain the component and its historical values.
    api_response = api_instance.component_get_guid_get(guid, index=index)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentApi->component_get_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **guid** | **str**| The unique identifier of the component. | 
 **index** | **int**| The &#x27;page&#x27; of the list of historical values in 100s | [optional] [default to 0]

### Return type

[**ComponentViewModel**](ComponentViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **component_update_put**
> str component_update_put(body=body)

Update a component.

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
api_instance = swagger_client.ComponentApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateComponentInputModel() # UpdateComponentInputModel | The supposed properties/parameters of the component. (optional)

try:
    # Update a component.
    api_response = api_instance.component_update_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ComponentApi->component_update_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateComponentInputModel**](UpdateComponentInputModel.md)| The supposed properties/parameters of the component. | [optional] 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

