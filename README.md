# When Autumn Comes 🍂
## 프로젝트 소개
*가을이 오면~ 눈부신 아침 햇살에 비친 그대의 미소가 아름다워요~*   
**가을**하면 가장 먼저 어떤 것이 떠오르시나요??  
보시다시피 저는 **이문세의 가을이 오면**이라는 노래가 가장 먼저 떠오릅니다.  
그렇습니다!! 가을은 선선하고 맑은 날씨와 함께 감성이 충만해지는 계절이기 때문에 노래도 많이 듣게 됩니다.  
<img src="https://drive.google.com/uc?id=169v_Nqh_krdvs3hgecYLaKHL4HJ5msiJ" width="300" height="300"/>  
When Autumn Comes는 (이하 WAC) 지금 내 기분이나 상태, 듣고 싶은 노래를 말하면, 구글 Cloud의 Speech-to-Text API를 이용해서 그것을 텍스트로 번역하고   
사용자가 듣고 싶어할만한 노래를 카카오의 OpenAPI를 이용한 "나와의 채팅"으로 카톡 메시지를 보내는 프로젝트입니다.  

## ✋ 시작하기에 앞서
WAC는 구글 Cloud와 카카오의 API를 사용했기 때문에 이 프로젝트를 사용하기 위해서는 이 둘의 서비스 인증 키를 받아야 합니다.  
### 0. 당연히 Github에 있는 모든 프로젝트 파일들을 다운 받아 주세요.
 #### 1. 먼저 카카오톡의 REST API 키, 인증 코드, access token을 받아봅시다. 링크된 사이트를 따라 REST API키를 받고 설정까지 마쳐주세요. STEP 5는 생략하셔도 됩니다.  
[카카오톡 REST API 키 발급받고 설정하기](https://ai-creator.tistory.com/20)  
#### 2. REST API 키를 발급 받았으면 인증 코드를 받아보겠습니다. 인터넷 창을 시크릿 모드로 열고 REST API 키를 입력한 아래의 주소로 접속해주세요.  
`https://kauth.kakao.com/oauth/authorize?client_id=여기에 REST_API 키를 입력하세요&response_type=code&redirect_uri=https://localhost.com`  
2-2. 카카오톡 로그인 창이 나오면 로그인하시고, 약관에 동의해주세요.  
2-3. 잠시 기다렸다가  
<img src="https://img1.daumcdn.net/thumb/R1280x0/?scode=mtistory2&fname=https%3A%2F%2Fblog.kakaocdn.net%2Fdn%2F36luw%2FbtqDmmkC0Zk%2FPVoD3KzAjkP37nTFDUhZ8K%2Fimg.png" width="300" height="200"/>  
이런 창이 나오면 **?code=** 뒤에 빨간 부분을 복사해주세요. 이것이 "인증코드"입니다.  
2-4. 프로젝트 파일에 들어있는 *Restapi+code.txt*에 REST API키와 인증코드를 각각 입력하고 저장해주세요.  
2-5. 정해진 위치에 잘 저장하셨다면 **kakao_token.py**를 실행해주세요. 자동으로 access_token을 받아와 주고, 계속 쓸 수 있도록 **kakao_token.json**파일도 생성해줍니다.  
**(잠깐! 모든 access_token의 사용 가능 시간은 6시간입니다. 6시간이 지나면 refresh token을 이용한 *refresh_kakao.py*를 실행시켜 새로운 access_token을 받아주세요!!)**  
### 3. 이제 구글 Cloud의 Speech-to-Text API 키를 발급받아 보겠습니다.  

