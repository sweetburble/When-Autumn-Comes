def create_template(command):
    import random
    a, b = random.sample([0,1,2,3,4,5,6,7,8,9], 2) # 매번 다른 두 숫자를 고른다.

    if ("코딩" in command):
        with open('coding_list.txt', 'r') as f:
            list = f.readlines()
            first = list[0].split(', ')
            second = list[1].split(', ')
        template = {
        "object_type": "list",
        "header_title": "코딩할 때 듣기 좋은 노래",
        "header_link": {
            "web_url": "https://url.kr/fgj7nm",
            "mobile_web_url": "https://m.youtube.com"
            },
        "contents": [
            {
                    "title": first[0],
                    "description": first[1],
                    "image_url": first[2],
                    "image_width": 50, "image_height": 50,
                    "link": {
                        "web_url": first[3],
                        "mobile_web_url": first[3]
                    }
                },
            {
                    "title": second[0],
                    "description": second[1],
                    "image_url": second[2],
                    "image_width": 50, "image_height": 50,
                    "link": {
                        "web_url": second[3],
                        "mobile_web_url": second[3]
                    }
                }
            ],
        "buttons": [
            {
                    "title": "검색 결과 더보기",
                    "link": {
                        "web_url": "https://url.kr/fgj7nm",
                        "mobile_web_url": "https://m.youtube.com"
                    }
                }
            ]
        }

        return template



def do(speech):
    import json
    from urllib import response
    import requests

    # 공식 문서에 기재된 POST와 Host 정보를 조합하여 요청할 url 정의
    url = "https://kapi.kakao.com/v2/api/talk/memo/default/send"

    # 사용자 토큰, 문서에 기재된 Authorization 정보 기재, access token은 약 6시간 유효하다.
    headers = {
        "Authorization": "Bearer " + "K2cfeHPzsVIgythJze41hprhgYXpcORSzKbkLFb7CisM1AAAAYPHL6AG"
    }

    # template_object에 필수(Required)로 필수 요소 기재
    # template = {
    #     "object_type": "list",
    #     "header_title": "초밥 사진",
    #     "header_link": {
    #         "web_url": "www.naver.com",
    #         "mobile_web_url": "www.naver.com"
    #         },
    #     "contents": [
    #         {
    #                 "title": "1. 광어초밥",
    #                 "description": "광어는 맛있다",
    #                 "image_url": "https://i.ytimg.com/vi/Xc1Le3CSdrM/default.jpg",
    #                 "image_width": 50, "image_height": 50,
    #                 "link": {
    #                     "web_url": "www.naver.com",
    #                     "mobile_web_url": "www.naver.com"
    #                 }
    #             },
    #         {
    #                 "title": "2. 참치초밥",
    #                 "description": "참치는 맛있다",
    #                 "image_url": "https://search2.kakaocdn.net/argon/0x200_85_hr/IjIToH1S7J1",
    #                 "image_width": 50, "image_height": 50,
    #                 "link": {
    #                     "web_url": "www.naver.com",
    #                     "mobile_web_url": "www.naver.com"
    #                 }
    #             }
    #         ],
    #     "buttons": [
    #         {
    #                 "title": "웹으로 이동",
    #                 "link": {
    #                     "web_url": "www.naver.com",
    #                     "mobile_web_url": "www.naver.com"
    #                 }
    #             }
    #         ]
    #     }

    template = create_template("코딩입니다.")

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
    do("화이팅")