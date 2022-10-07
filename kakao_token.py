import requests
import json

url = "https://kauth.kakao.com/oauth/token"

data = {
    "grant_type" : "authorization_code",
    "client_id" : "8090f2bd028126297e9ca00ed16d4ea0",
    "redirect_uri" : "https://localhost.com",
    "code"         : "0N3mPRaLG-lw2wEcmJ3ih9UAkhO8z2mucMLkhpMK4m0_i3yOV7z8G2SBmPrQo9_eiiVIogopcFEAAAGDskU_2A"
    
}
response = requests.post(url, data=data)

tokens = response.json()

print(tokens)

with open("kakao_token.json", "w") as fp:
    json.dump(tokens, fp)


# access token의 유효시간이 지나면, refresh token을 이용해서 재발급 받아야 합니다.
# url = "https://kauth.kakao.com/oauth/token"
# data = {
#     "grant_type" : "refresh_token",
#     "client_id"  : "<REST_API 앱키를 입력하세요>",
#     "refresh_token" : "<refresh token을 입력하세요>"
# }
# response = requests.post(url, data=data)

# print(response.json())