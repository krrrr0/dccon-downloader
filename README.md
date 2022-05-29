# 디시콘 다운로더
## 개요
디시콘 번호를 이용하여 로컬에 디시콘 패키지를 다운로드합니다.  
`aiohttp`을 사용하여 구현되어서 매우 빠른 속도를 자랑합니다.  
  
**파이썬 3.9 환경에서 테스트 되었습니다. 이전 버전에서는 작동하지 않을 수 있습니다.**

## 셋업하기
### 1. 저장소를 로컬에 클론합니다.
```
$ git clone https://github.com/krrrr0/dccon-downloader.git
$ cd dccon-downloader
```

### 2. 가상 환경을 설정하고, 의존성을 설치합니다.
```
2.1. virtualenv를 설치합니다.
$ pip install virtualenv

2.2. 가상 환경을 만듭니다.
$ virtualenv venv

2.3. 가상 환경을 활성화합니다.
- 리눅스의 경우:
$ source venv/bin/activate
- 윈도우의 경우:
$ venv/Scripts/activate

2.4. 의존성을 설치합니다.
$ pip install -r requirements.txt
```

## 사용법
```
- 기본
python ./main.py 86920

- 지정된 디렉토리에 다운로드
python ./main.py 86920 E:/dccon
```

## 도와주세요!
Issue 탭으로 가셔서 새로운 이슈를 등록하시기 바랍니다.  
**이슈 작성 시에 반드시 포함해야 하는 내용:**
- 컴퓨터 OS
- 파이썬 버전 `python -V`로 확인
- (오류가 발생한 경우) 전체 Traceback


## TODO
- pypi 패키지 퍼블리싱


## 라이선스
리포지토리의 코드는 MIT 라이선스로 배포됩니다. 다른 프로젝트에서 사용하게 될 경우, 다음과 같은 인용을 사용하세요:
```
예시:

dccon-downloader (https://github.com/krrrr0/dccon-downloader)
(c) 2022 krrrr0
Released under the MIT License.
```
