import requests
import json

url = "https://kauth.kakao.com/oauth/token"
app_key = "8090f2bd028126297e9ca00ed16d4ea0"

# data = {
#     "grant_type" : "authorization_code",
#     "client_id" : app_key,
#     "redirect_uri" : "https://localhost.com",
#     "code"         : "ZZihgIDFhGsgn3emAgd1I2VBnmCihD76KHwVMRZFNscaiiSjqOE0JujzWDbCO7wQ5UkIDgopyNgAAAGDxy6eaA"
    
# }
# response = requests.post(url, data=data)

# tokens = response.json()

# print(tokens)

# with open("kakao_token.json", "w") as fp:
#     json.dump(tokens, fp)
# print(response.json())

# access token의 유효시간이 지나면, refresh token을 이용해서 재발급 받아야 합니다.
# 한 access token의 유효시간은 약 6시간 정도입니다.
with open("kakao_token.json", "r") as fp:
    tokens = json.load(fp)
data = {
    "grant_type" : "refresh_token",
    "client_id"  : app_key,
    "refresh_token" : tokens["refresh_token"]
}
response = requests.post(url, data=data)
cur_tokens = response.json()
print(response.status_code)
print(response.json())
tokens["access_token"] = cur_tokens["access_token"]
tokens["app_key"] = app_key

with open("kakao_token.json", "w") as fp:
    json.dump(tokens, fp)