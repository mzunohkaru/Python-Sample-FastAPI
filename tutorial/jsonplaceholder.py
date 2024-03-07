import requests
url = 'https://jsonplaceholder.typicode.com/posts'

res = requests.get(url)

print(res.status_code)

allData = res.json()
firstData = allData[0]
firstDataUser = firstData['userId']

print(firstDataUser)

params = {
    'id': 3
}

resParameter = requests.get(url, params)
parameterData = resParameter.json()

print(parameterData)