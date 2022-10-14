# When Autumn Comes 🍂
## 프로젝트 소개
*가을이 오면~ 눈부신 아침 햇살에 비친 그대의 미소가 아름다워요~*<br/><br/> 
**가을**하면 가장 먼저 어떤 것이 떠오르시나요??  
보시다시피 저는 **이문세의 가을이 오면**이라는 노래가 가장 먼저 떠오릅니다.  
그렇습니다!! 가을은 선선하고 맑은 날씨와 함께 감성이 충만해지는 계절이기 때문에 노래도 많이 듣게 됩니다.  
<img src="https://drive.google.com/uc?id=169v_Nqh_krdvs3hgecYLaKHL4HJ5msiJ" width="300" height="300"/><br/>  
When Autumn Comes(이하 WAC)는 지금 내 기분이나 상태, 듣고 싶은 노래를 말하면, 구글 Cloud의 Speech-to-Text API를 이용해서 그것을 텍스트로 번역하고   
사용자가 듣고 싶어할만한 노래를 카카오의 OpenAPI를 이용한 "나와의 채팅"으로 카톡 메시지를 보내는 프로젝트입니다.  
<br/><br/>
## ✋ 시작하기에 앞서
WAC는 구글 Cloud와 카카오의 API를 사용했기 때문에 이 프로젝트를 사용하기 위해서는 이 둘의 서비스 인증 키를 받아야 합니다.  
### 0. 당연히 Github에 있는 모든 프로젝트 파일들을 다운 받아 주세요.
 #### 1. 먼저 카카오톡의 REST API 키, 인증 코드, access token을 받아봅시다. 링크된 사이트를 따라 REST API키를 받고 설정까지 마쳐주세요. STEP 5는 생략하셔도 됩니다.  
[카카오톡 REST API 키 발급받고 설정하기](https://ai-creator.tistory.com/20)  
#### 2. REST API 키를 발급 받았으면 인증 코드를 받아보겠습니다. 인터넷 창을 시크릿 모드로 열고 REST API 키를 입력한 아래의 주소로 접속해주세요.
```  
https://kauth.kakao.com/oauth/authorize?client_id=여기에 REST_API 키를 입력하세요&response_type=code&redirect_uri=https://localhost.com 
``` 
2-2. 카카오톡 로그인 창이 나오면 로그인하시고, 약관에 동의해주세요.  
2-3. 잠시 기다렸다가  
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F36luw%2FbtqDmmkC0Zk%2FPVoD3KzAjkP37nTFDUhZ8K%2Fimg.png" width="300" height="200"/>  
이런 창이 나오면 **?code=** 뒤에 빨간 부분을 복사해주세요. 이것이 "인증코드"입니다.  
2-4. 프로젝트 파일에 들어있는 *Restapi+code.txt*에 REST API키와 인증코드를 각각 입력하고 저장해주세요.  
2-5. 정해진 위치에 잘 저장하셨다면 **kakao_token.py**를 실행해주세요. 자동으로 access_token을 받아와 주고, 계속 쓸 수 있도록 **kakao_token.json**파일도 생성해줍니다.  
**(잠깐! 모든 access_token의 사용 가능 시간은 6시간입니다. 6시간이 지나면 refresh token을 이용한 *refresh_kakao.py*를 실행시켜 새로운 access_token을 받아주세요!!)**<br/><br/>
### 3. 이제 구글 Cloud의 Speech-to-Text API 키를 발급받아 보겠습니다.  
링크된 사이트에 접속하여 "1. Clude Speech API 키 발급받기" "2. Cloud SDK 설치"까지만 따라해주세요.   
[구글 Cloud API 사용해보기](https://webnautes.tistory.com/1247)  
3-2. 자신의 파이썬 가상환경 터미널을 준비하고 실행시켜 주세요. (예: Anaconda prompt)  
3-3. 다음 명령어들을 차례로 입력해주세요.  
```python
pip install --upgrade google-cloud-storage

pip install google-cloud-speech
```
3-4. 여러분의 구글 클라우드 서비스 계정 키가 위치한 경로를 잘 숙지하시고 아래 명령어를 입력해주세요. 키가 담긴 json 파일을 우클릭 한다음 **경로로 복사**를 하면 편합니다. 
```
c:\google-cloud-sdk\bin\gcloud auth activate-service-account --key-file="C:\Users\내 윈도우 계정\Downloads\서비스 계정키.json

예를 들면 이런식으로 명령어를 입력하시면 됩니다.
c:\google-cloud-sdk\bin\gcloud auth activate-service-account --key-file="C:\Users\Bandi\Downloads\when-autumn-comes-65765516efe.json"
```

3-5. 마이크 사용을 위해 필요한 패키지인 [pyaudio](https://www.lfd.uci.edu/~gohlke/pythonlibs/#pyaudio) 를 설치합니다.  
위 링크에서 자신의 파이썬 가상환경 버전에 맞는 파일을 다운로드 합니다.  
예를 들어 Python 3.9.X의 경우 PyAudio-0.2.11-cp39-cp39m-win_amd64.whl를 다운로드 합니다.  
다음 처럼 다운로드 받은 파일 위치를 지정하여 설치합니다.  
```
pip install ..\Downloads\PyAudio-0.2.11-cp39-cp39m-win_amd64.whl
```  
### 4. 수고하셨습니다. 이제 recording_cloud.py를 실행하여 여러분의 감정을 솔직하게 말씀해주시고 그에 맞는 플레이리스트를 추천받아 보세요!  
<br/><br/><br/>

## 🚒 발생할 수 있는 에러와 해결법<br/>
<img width="626" alt="access 토큰 만료" src="https://user-images.githubusercontent.com/79733289/195757810-748505f9-70cb-4463-a034-fabf34b04268.png">
recording_cloud.py를 실행했을 때 발생하는 에러로 카카오톡의 **access_token이 만료**된 상황입니다.
**refresh_token.py를 실행**시켜서 다시 access_token을 받아주세요.
<br/><br/><br/>
<img width="506" alt="리프레쉬 토큰 오류" src="https://user-images.githubusercontent.com/79733289/195760417-c4705578-72ea-44af-9d4c-de6ada1083b0.png">
refresh_token.py를 실행했을 때 발생하는 에러로<br/>
"시작하기에 앞서" 챕터로 돌아가 2번 항목을 다시 수행하여 **새 인증 코드와 새 access_token**을 받아주세요.
<br/><br/><br/>
<img width="429" alt="키워드와 다른 명령을 했을때" src="https://user-images.githubusercontent.com/79733289/195760888-532fed15-4140-4ce4-91e4-0473018a1777.png">
WAC는 사용자의 노래 취향을 **올바르게 저격**할 수 있도록 키워드가 한정되어 있습니다.<br/>
정해진 키워드가 들어간 문장을 말해주시면 감사하겠습니다.

<br/><br/><br/>
## 🎶 WAC야, 노래 추천해줘
#### 현재 WAC가 추천해줄 수 있는 키워드는 8가지입니다!! (추후 추가 예정)<br/><br/>
먼저 여러분의 현재 기분이나 듣고 싶은 노래가 있으면<br/>
### "코딩" "게임" "가을" "우울" "심심" "시티팝" "비 오는 날" 그리고 "추천"에 맞춰서 말해보세요!<br/>
#### WAC가 제대로 파악하여 엄선한 노래들을 추천합니다.
<img width="284" alt="코딩" src="https://user-images.githubusercontent.com/79733289/195763462-b5e0acf0-f97d-446a-b476-0b407885d178.png"><img width="287" alt="가을" src="https://user-images.githubusercontent.com/79733289/195763558-3bb179f0-2143-4095-b762-5c253461ba58.png"><br/>
<img width="285" alt="우울" src="https://user-images.githubusercontent.com/79733289/195763624-09ef08fb-346b-4235-ab97-72fdc847aff3.png"><img width="282" alt="추천" src="https://user-images.githubusercontent.com/79733289/195763654-815be928-a8d3-444d-bf81-226e631c3e85.png">
<br/><br/>
### 내 마음을 설레게 할 노래부터 공부에 집중할 수 있는 노래까지..! 올 가을 WAC과 함께 즐겁게 보내시길 바랍니다.<br/><br/>
## 감사합니다 👋
<br/><br/><br/>
## Reference 👍
[카카오 공식문서](https://developers.kakao.com/) - 카카오 메시지 API 및 튜토리얼, 오류 코드 제공

[ai-creator님의 블로그](https://ai-creator.tistory.com/23) - 카카오톡 "나와의 채팅" 기능 구현

[멈춤보단 천천히라도님의 블로그](https://webnautes.tistory.com/1247) - Google Cloud Speech-to-Text API 사용 방법

https://gist.github.com/mabdrabo/8678538 - pyaudio를 사용한 녹음 기능

<br/><br/>
## License 📋
Apache license 2.0  
LICENSE 파일에 포함되어 있습니다.]
