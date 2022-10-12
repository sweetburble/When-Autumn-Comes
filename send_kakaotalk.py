def create_template(command):
    import random
    a, b = random.sample([0,1,2,3,4,5,6,7,8,9], 2) # 매번 다른 두 숫자를 고른다.

    if ("코딩" in command):
        with open('coding_list.txt', 'r') as f:
            list = f.readlines()
            first = list[a].split(', ')
            second = list[b].split(', ')

        return first, second, "코딩할 때 집중하기 좋은 노래", "https://url.kr/fgj7nm"
    
    elif ("게임" in command):
        with open('game_list.txt', 'r') as f:
            list = f.readlines()
            first = list[a].split(', ')
            second = list[b].split(', ')

        return first, second, "게임할 때 듣기 좋은 신나는 노래", "https://url.kr/px9i1h"



def do(speech):
    import json
    from urllib import response
    import requests

    # 공식 문서에 기재된 POST와 Host 정보를 조합하여 요청할 url 정의
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    # 사용자 토큰, 문서에 기재된 Authorization 정보 기재, access token은 약 6시간 유효하다.
    headers = {
        "Authorization": "Bearer " + "rpT3FMq5LWRUBkAh-Q0qijWBirxtCAyuelPuui00Cj10lwAAAYPMPf_H"
    }

    # 음성인식 결과를 create_template의 매개 변수로 제공하고, 여러가지 값들을 리턴받는다.
    first, second, header, default_link = create_template(speech)

    # template_object에 필수(Required)로 되어있는 요소를 create_template 함수에서 받은 값으로 기재
    template = {
        "object_type": "list",
        "header_title": header,
        "header_link": {
            "web_url": default_link,
            "mobile_web_url": default_link
            },
        "contents": [
            {
                    "title": first[0],
                    "description": "Youtube",
                    "image_url": first[1],
                    "image_width": 50, "image_height": 50,
                    "link": {
                        "web_url": first[2],
                        "mobile_web_url": first[2]
                    }
                },
            {
                    "title": second[0],
                    "description": "Youtube",
                    "image_url": second[1],
                    "image_width": 50, "image_height": 50,
                    "link": {
                        "web_url": second[2],
                        "mobile_web_url": second[2]
                    }
                }
            ],
        "buttons": [
            {
                    "title": "검색 결과 더보기",
                    "link": {
                        "web_url": default_link,
                        "mobile_web_url": default_link
                    }
                }
            ]
        }

    # template 변수를 json string 형식으로 변경
    data = {
        "template_object": json.dumps(template)
        }

    # 요청
    response = requests.post(url, data=data, headers=headers)

    # 에러 코드 확인
    print(response.status_code)
    if response.json().get('result_code') == 0:
            print("메시지를 성공적으로 보냈습니다.")
    else:
            print(f"메시지를 성공적으로 보내지 못했습니다. 오류메시지 : {str(response.json())}")

if (__name__ == "__main__"):
    do("코딩할때 듣기 좋은 노래")