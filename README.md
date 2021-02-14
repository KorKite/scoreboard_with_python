# scoreboard_with_python
    파이썬으로 구현한 score board입니다.
<img width="880" alt="스크린샷 2021-02-14 오후 6 47 33" src="https://user-images.githubusercontent.com/50725139/107873339-2020de80-6ef5-11eb-8e2e-9311f91cb795.png">

  
## Language Needed
    1. NodeJS -> TailwindCSS
    2. Python3 -> Flask

## How to Start
    1. 아래의 customization을 보고 본인에게 맞게 설정을 변경 
    2. python3 main.py # 서버 시작 / 이것만 키면 다른건 안건들여도 됨
    3. 만약 tailwind설정으 변경하고 싶은 경우 -> npm으로 tailwind설치하여 시작

## Customization
    1. answer.csv -> 정답이 되는 csv파일을 answer.csv와 동일한 형식으로 넣어주어야 함
    
    2. scoring.py
      -> f1_score를 accuracy의 지표로 설정할 수 있다. 
      -> answer.csv 형식이나 길이가 바뀌면 scoring.py에서 shape을 변경해주어야 한다.
    
    3. scoring.py (db관련)
      -> mongodb를 활용하였기 때문에, 설정을 변경해주어야 한다.
    
    4. templates/footer.html
      -> 수업명으로 변경하여 사용하면 된다.

## Database (Mongo DB)
    MongoDB 몽고디비를 사용하여 score를 기록하였다.
    제출시 수집하고 데이터베이스에 기록하는 정보는
    1. 유저의 ip
    2. 등록한 이름
    3. 업로드하 파일명
    4. 생성시간
    5. 정확도
    이다. ip의 경우, 부정행위가 발생하 경우, 수집한 ip를 기반으로 검증할 수 있다.

## Architecutre
### Folders
    templates: HTML files
    static: css files
    assets: for tailwind css
    reported: 제출된 파일들 모음
  
### Python Files
    main.py -> python3 main.py로 이 파일을 실행하면 서버가 켜짐
    scoring.py -> 정답과 입력을 비교해서 점수를 계산하고 데이터베이스에 저장하는 함수

### Javascript Files
    package.json -> Nodejs 설정
    tailwind.config.js -> tailwindcss 설정
    gulpfile.js -> tailwindcss를 위한 파일
  
  
