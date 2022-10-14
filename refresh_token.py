# access token의 유효시간이 지나면, refresh token을 이용해서 재발급 받아야 합니다.
# 한 access token의 유효시간은 약 6시간 정도입니다.

import requests
import json

# 사용자가 얻은 REST API Key를 텍스트 파일에 넣기만 하면, 읽어와서 저장합니다.
with open('Restapi+code.txt', 'r') as f:
            lines = f.readlines()
            lines = list(map(lambda s: s.strip(), lines)) # 텍스트 파일에는 개행문자가 포함되기 때문에
            API_KEY = lines[1]

url = "https://kauth.kakao.com/oauth/token"

with open("kakao_token.json", "r") as fp:
    tokens = json.load(fp)

data = {
    "grant_type" : "refresh_token",
    "client_id"  : API_KEY,
    "refresh_token" : tokens['refresh_token']
}

response = requests.post(url, data=data)
new_token = response.json()
print(response.status_code)
print(response.json())
tokens['access_token'] = new_token['access_token']
tokens['API_KEY'] = API_KEY

with open("kakao_token.json", "w") as fp:
    json.dump(tokens, fp)