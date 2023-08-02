import configuration
import requests
import data




def post_new_client(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,  # подставляем полный url
                         json=body,  # тут тело
                         headers=data.headers)  # а здесь заголовки
response = post_new_client(data.user_body);
print(response.status_code)
token = response.json()['authToken']





def post_new_client_set(body, auth_token):
    #в переменную добавляется копия data.headers()
    headers_set = data.headers.copy()
    #в переменную добавляется токен
    headers_set["Authorization"] = "Bearer " + auth_token
    print(auth_token)
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_SET_KITS_PATH,json=body, headers= headers_set)












