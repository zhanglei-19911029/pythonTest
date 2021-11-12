import requests

res = requests.post(url='https://fanyi.baidu.com/sug', data={"kw": "hello"})
print(res.json()['data'][0]['v'])
