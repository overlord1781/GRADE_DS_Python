import requests

url = 'https://reqres.in/api/users?page=2'
# Получение статус кода
def get_status_code(url):
    status_code = requests.get(url).status_code
    return print(status_code)

# Получение json ответа
def get_request(url):
    r = requests.get(url)
    print(r.json())

# Получение параметров сервера
def option_request(url):
    r = requests.options(url)
    print(r.headers)

# Получение параметров сервера
def post_request(url,dict):
    r = requests.post(url,dict)
    print(r.json())

def put_request(url, data):
    r = requests.put(url, data)
    print(r.json())

def patch_request(url, data):
    r = requests.patch(url, data)
    print(r.json())

def delete_request(url):
    r = requests.delete(url)
    print(r.headers)

get_status_code(url)
get_request(url)
option_request(url)

data = {
    "name": "Mark",
    "job": "Tester"
}
post_request('https://reqres.in/api/users', data)
put_request('https://reqres.in/api/users/2', data)
patch_request('https://reqres.in/api/users/2', data)
delete_request('https://reqres.in/api/users/2')