# swagger_client.ItemApi

All URIs are relative to *https://api.nozomi.ai*

Method | HTTP request | Description
------------- | ------------- | -------------
[**item_all_index_get**](ItemApi.md#item_all_index_get) | **GET** /Item/All/{index} | Obtains all of the relevant items you own.
[**item_create_post**](ItemApi.md#item_create_post) | **POST** /Item/Create | Create an item.
[**item_exists_slug_get**](ItemApi.md#item_exists_slug_get) | **GET** /Item/Exists/{slug} | Validates if the slug is being used.
[**item_get_by_slug_slug_get**](ItemApi.md#item_get_by_slug_slug_get) | **GET** /Item/GetBySlug/{slug} | Obtains the specified item.
[**item_get_item_guid_get**](ItemApi.md#item_get_item_guid_get) | **GET** /Item/Get/{itemGuid} | Obtains the specified item.
[**item_update_put**](ItemApi.md#item_update_put) | **PUT** /Item/Update | Update the specified item.

# **item_all_index_get**
> ItemViewModelIEnumerablePaginatedViewModel item_all_index_get(index, parent_guid_filter, slug_filter, name_filter)

Obtains all of the relevant items you own.

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
api_instance = swagger_client.ItemApi(swagger_client.ApiClient(configuration))
index = 56 # int | The 'page' of the list of results of every x items.
parent_guid_filter = 'parent_guid_filter_example' # str | Filters items by Parent ID.
slug_filter = 'slug_filter_example' # str | Filters items by slug.
name_filter = 'name_filter_example' # str | Filters items by name.

try:
    # Obtains all of the relevant items you own.
    api_response = api_instance.item_all_index_get(index, parent_guid_filter, slug_filter, name_filter)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_all_index_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **index** | **int**| The &#x27;page&#x27; of the list of results of every x items. | 
 **parent_guid_filter** | **str**| Filters items by Parent ID. | 
 **slug_filter** | **str**| Filters items by slug. | 
 **name_filter** | **str**| Filters items by name. | 

### Return type

[**ItemViewModelIEnumerablePaginatedViewModel**](ItemViewModelIEnumerablePaginatedViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_create_post**
> str item_create_post(body=body)

Create an item.

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
api_instance = swagger_client.ItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.CreateItemInputModel() # CreateItemInputModel | The supposed properties/parameters of the item. (optional)

try:
    # Create an item.
    api_response = api_instance.item_create_post(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_create_post: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**CreateItemInputModel**](CreateItemInputModel.md)| The supposed properties/parameters of the item. | [optional] 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_exists_slug_get**
> bool item_exists_slug_get(slug, local=local)

Validates if the slug is being used.

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
api_instance = swagger_client.ItemApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | The unique identifier of the item.
local = false # bool | If you want to only check the slugs you own. (optional) (default to false)

try:
    # Validates if the slug is being used.
    api_response = api_instance.item_exists_slug_get(slug, local=local)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_exists_slug_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| The unique identifier of the item. | 
 **local** | **bool**| If you want to only check the slugs you own. | [optional] [default to false]

### Return type

**bool**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_get_by_slug_slug_get**
> ItemViewModel item_get_by_slug_slug_get(slug)

Obtains the specified item.

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
api_instance = swagger_client.ItemApi(swagger_client.ApiClient(configuration))
slug = 'slug_example' # str | The unique slug of the item.

try:
    # Obtains the specified item.
    api_response = api_instance.item_get_by_slug_slug_get(slug)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_get_by_slug_slug_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **slug** | **str**| The unique slug of the item. | 

### Return type

[**ItemViewModel**](ItemViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_get_item_guid_get**
> ItemViewModel item_get_item_guid_get(item_guid)

Obtains the specified item.

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
api_instance = swagger_client.ItemApi(swagger_client.ApiClient(configuration))
item_guid = 'item_guid_example' # str | The unique identifier of the item.

try:
    # Obtains the specified item.
    api_response = api_instance.item_get_item_guid_get(item_guid)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_get_item_guid_get: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **item_guid** | **str**| The unique identifier of the item. | 

### Return type

[**ItemViewModel**](ItemViewModel.md)

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **item_update_put**
> str item_update_put(body=body)

Update the specified item.

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
api_instance = swagger_client.ItemApi(swagger_client.ApiClient(configuration))
body = swagger_client.UpdateItemInputModel() # UpdateItemInputModel | The supposed properties/parameters the value you want to update on an item. (optional)

try:
    # Update the specified item.
    api_response = api_instance.item_update_put(body=body)
    pprint(api_response)
except ApiException as e:
    print("Exception when calling ItemApi->item_update_put: %s\n" % e)
```

### Parameters

Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **body** | [**UpdateItemInputModel**](UpdateItemInputModel.md)| The supposed properties/parameters the value you want to update on an item. | [optional] 

### Return type

**str**

### Authorization

[API Key](../README.md#API Key)

### HTTP request headers

 - **Content-Type**: application/json, text/json, application/*+json
 - **Accept**: text/plain, application/json, text/json

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

