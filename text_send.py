import json
import requests

# 공식 문서에 기재된 POST와 Host 정보를 조합하여 요청할 url 정의
url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

# 사용자 토큰, 문서에 기재된 Authorization 정보 기재
headers = {
    "Authorization": "Bearer " + "rpT3FMq5LWRUBkAh-Q0qijWBirxtCAyuelPuui00Cj10lwAAAYPMPf_H"
}

# template_object에 필수(Required)로 필수 요소 기재
data = { 
    "template_object" : json.dumps({ "object_type" : "text",
                                    "text" : "Hello, world!",
                                    "link" : {
                                        "web_url" : "https://www.daum.net/"
                                    }
    })
}

# 요청 및 에러코드 확인 (HTTP 상태 코드는 200이 성공)
response = requests.post(url, headers=headers, data=data)
print(response.status_code)

if response.json().get('result_code') == 0:
    print("메시지를 성공적으로 보냈습니다.")
else:
    print(f"메시지를 성공적으로 보내지 못했습니다. 오류메시지 : {str(response.json())}")