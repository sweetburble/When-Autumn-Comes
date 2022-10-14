import requests
import json

# 사용자가 얻은 REST API Key와 인증 코드를 텍스트 파일에 넣기만 하면, 읽어와서 저장합니다.
with open('Restapi+code.txt', 'r') as f:
            lines = f.readlines()
            lines = list(map(lambda s: s.strip(), lines)) # 텍스트 파일에는 개행문자가 포함되기 때문에
            API_KEY = lines[1]
            Authentication_Code = lines[4]

print(API_KEY)
print(Authentication_Code)

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : API_KEY,
    "redirect_uri" : "https://localhost.com",
    "code"         : Authentication_Code
}

response = requests.post(url, data=data)

tokens = response.json()

print(tokens)

with open("kakao_token.json", "w") as fp:
    json.dump(tokens, fp)

# access token의 유효시간이 지나면, refresh token을 이용해서 재발급 받아야 합니다.
# 한 access token의 유효시간은 약 6시간 정도입니다.