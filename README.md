# Raspberry Pi를 이용한 파이썬 게임 프로젝트 (개인 프로젝트)


<p align="center">

<img src="https://private-user-images.githubusercontent.com/79098475/351939207-f375d82b-366e-4748-8a79-afbd6cb58ba7.svg?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4Nzc3MzksIm5iZiI6MTcyMTg3NzQzOSwicGF0aCI6Ii83OTA5ODQ3NS8zNTE5MzkyMDctZjM3NWQ4MmItMzY2ZS00NzQ4LThhNzktYWZiZDZjYjU4YmE3LnN2Zz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDAzMTcxOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWYyMDk1ZThjOGQ0NzEwNzNiMGVmY2JkMTFlMDQ0YmY3OTJjMzQ4YTU1NGYwNThlYmJiMWY3NWNlN2EyMDEyODkmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.6-9LQSReOBOrvzGkOZfUfn0bIgOfbfEYGdPYPYra8Rk" alt="라즈베리파이 로고" width="12%" />
</p>

임베디드 SW라는 과목을 수강하면서 라즈베리파이로 게임을 만드는 프로젝트를 하게 되었다. <br>
이 프로젝트를 통해 **객체지향 프로그래밍 기법**과 **파이썬 이미지 처리**에 대한 실력을 늘리고 싶었다. <br>
또한 **시각적으로 흥미**를 끌만한 게임을 만들고 싶었다. <br>
어렸을 때 플래시 게임으로 짱구 볼링게임을 한적이있는데, 이를 모티브로 하여 추가적인 재미요소 또한 구현하기로 하였다. 

## Preview

<p style="display: flex; justify-content: center; overflow-x: auto; white-space: nowrap;">
 
<img src="https://private-user-images.githubusercontent.com/79098475/351943497-9477192e-3f84-4a9a-8d62-04e73f0e2f47.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4Nzc3MzksIm5iZiI6MTcyMTg3NzQzOSwicGF0aCI6Ii83OTA5ODQ3NS8zNTE5NDM0OTctOTQ3NzE5MmUtM2Y4NC00YTlhLThkNjItMDRlNzNmMGUyZjQ3LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDAzMTcxOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTM2ZDA0Y2FlMGM5ZGFkNWFiZDRkNDc5YmJkNzI2MzVmZWRmM2EzYjMwYTgwZTk1ZDJhZmVmMWZkNWVmYTQ3N2MmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.KF3yqW5gvbJNndxE4TbOFi5znO2yYv1g_5p0oipnXmQ" style="display: inline-block; width: auto; height: 160px;">
<img src="https://private-user-images.githubusercontent.com/79098475/351944261-a5761a38-242b-4e2b-894c-f20245ea2f13.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4Nzc3MzksIm5iZiI6MTcyMTg3NzQzOSwicGF0aCI6Ii83OTA5ODQ3NS8zNTE5NDQyNjEtYTU3NjFhMzgtMjQyYi00ZTJiLTg5NGMtZjIwMjQ1ZWEyZjEzLmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDAzMTcxOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWM5NGMwOTA2N2ViOTQwZjUwNWFiYjcyMzg3ZjYxNThiMmE1ODU1NjUxY2VhNGU3Y2Q1MzcwYmY4MjIyMTg0YzYmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.hsqZ_3ex6_yccLc1ba5SyncCnj68b5imkA7yFFbchdw" style="display: inline-block; width: auto; height: 160px;">
<img src="https://private-user-images.githubusercontent.com/79098475/351944295-34b39cb7-32f3-43f5-9093-90ff72541a07.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4Nzc3MzksIm5iZiI6MTcyMTg3NzQzOSwicGF0aCI6Ii83OTA5ODQ3NS8zNTE5NDQyOTUtMzRiMzljYjctMzJmMy00M2Y1LTkwOTMtOTBmZjcyNTQxYTA3LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDAzMTcxOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTY2NjBiZmQ3YmY4N2IwMzhjY2I2MWNhNzVkZjc1ZTU1Yjk1MDkzNTIzZDY0M2JhMDhhYmM0ZTUyYjc4ZDJhNjAmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.JJBkZ1dPf4WBPNfhzL-kRtK0KIM6zXVPY5kuhKt7yRg" style="display: inline-block; width: auto; height: 160px;">
<img src="https://private-user-images.githubusercontent.com/79098475/351944543-598d95bb-46b6-4d42-a6c7-306b53547426.gif?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4Nzc3MzksIm5iZiI6MTcyMTg3NzQzOSwicGF0aCI6Ii83OTA5ODQ3NS8zNTE5NDQ1NDMtNTk4ZDk1YmItNDZiNi00ZDQyLWE2YzctMzA2YjUzNTQ3NDI2LmdpZj9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDAzMTcxOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPTNhNDk3YjJhMTIzZjEwN2Y0ZmNkZWZiMjIxYjEwMTg0YjJhN2ZjNjZmNzY3NmVmY2NmYjVjZmUzMTkyNGYzN2YmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.1C36qzU3v9EtTlgixIXfJgo3B_WhSKZR7akBZnc20zc" style="display: inline-block; width: auto; height: 160px;">

</p>

## Libraries

<div align="center">

![Static Badge](https://img.shields.io/badge/Linux-%23ACF600?logo=linux)
![Static Badge](https://img.shields.io/badge/raspberrypi-%23A22846?logo=raspberrypi)
![Static Badge](https://img.shields.io/badge/Adafruit-black?logo=Adafruit)
<br>
![Static Badge](https://img.shields.io/badge/Python-%23FFFFFF?logo=python)
![Static Badge](https://img.shields.io/badge/OpenCv-%235C3EE8?logo=opencv)
![Static Badge](https://img.shields.io/badge/PIL-%23500E00)
![Static Badge](https://img.shields.io/badge/Digitalio-violet)

</div>


## Development

- **객체 지향 프로그래밍**

게임 내에 등장하는 여러 객체들(볼링공, 볼링핀, 짱구 캐릭터) 간의 상호작용을 구현 <br>
이미지의 좌표를 계산하여 객체의 움직임에 따라 객체들이 어떻게 상호작용하는 지를 결정함 <br>
효율적인 모듈 관리를 위해 객체들과 여러 Asset들을 모듈화하여 코드를 작성하였음 <br>
 >  **짱구의 손 위치에서 볼링공이 출발하며 볼링공이 볼링핀의 어느 위치에서 맞는지에 따라 핀이 쓰러지는 방향이 달라지고, 쓰러진 핀에 의해 휩쓸리는 핀 또한 존재**


<p align="center">

  <img src="https://github.com/classaen7/RaspberryPI_Bowling/blob/master/Assets/zzangu1step.png?raw=true" alt="짱구자세1" width="12%" />
<span style="display:inline-block; width:10px;"></span>
  <img src="https://github.com/classaen7/RaspberryPI_Bowling/blob/master/Assets/zzangu2step.png?raw=true" alt="짱구자세2" width="14%" />
<span style="display:inline-block; width:20px;"></span>
<img src="https://github.com/classaen7/RaspberryPI_Bowling/blob/master/Assets/pin1.png?raw=true" alt="핀" width="4%" />
 <span style="display:inline-block; width:60px;"></span>
<img src="https://github.com/classaen7/RaspberryPI_Bowling/blob/master/Assets/mid_ball2.png?raw=true" alt="볼링공" width="5%" />


</p>


- **파이썬 이미지 표현**

라즈베리 파이는 매우 작은 디스플레이 화면이라는 **제약사항**이 존재함 <br>
이미지를 픽셀단위의 작은 크기로 조정하는 작업을 수행함 <br>
라즈베리 파이에서 구동가능한  다양한 라이브러리 활용

- **다양한 Use Case**

라즈베리파이는 `main.py`이 반복문처럼 **무한히 반복되는 구조**로 작동함 <br>
이러한 구조 속에서 사용자와 원활한 상호작용을하도록 다양한 Use Case를 구상하여 조건들을 처리하였음 <br>
이를 **FlowChart**로 표현하면 다음과 같음<br>
<p align="center">
<img src="https://private-user-images.githubusercontent.com/79098475/351938284-35bd5c53-5600-4e8a-abd2-e8e00324f73d.png?jwt=eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJpc3MiOiJnaXRodWIuY29tIiwiYXVkIjoicmF3LmdpdGh1YnVzZXJjb250ZW50LmNvbSIsImtleSI6ImtleTUiLCJleHAiOjE3MjE4Nzc3MzksIm5iZiI6MTcyMTg3NzQzOSwicGF0aCI6Ii83OTA5ODQ3NS8zNTE5MzgyODQtMzViZDVjNTMtNTYwMC00ZThhLWFiZDItZThlMDAzMjRmNzNkLnBuZz9YLUFtei1BbGdvcml0aG09QVdTNC1ITUFDLVNIQTI1NiZYLUFtei1DcmVkZW50aWFsPUFLSUFWQ09EWUxTQTUzUFFLNFpBJTJGMjAyNDA3MjUlMkZ1cy1lYXN0LTElMkZzMyUyRmF3czRfcmVxdWVzdCZYLUFtei1EYXRlPTIwMjQwNzI1VDAzMTcxOVomWC1BbXotRXhwaXJlcz0zMDAmWC1BbXotU2lnbmF0dXJlPWRjYmYyZDNjYTVkN2ExMzJlYzFmMWViMjk2ZTU5MDRkODM2NDE1NjEwZWEyNmY0NzBhMjM1YjE5N2JiNWExNzQmWC1BbXotU2lnbmVkSGVhZGVycz1ob3N0JmFjdG9yX2lkPTAma2V5X2lkPTAmcmVwb19pZD0wIn0.kEv4iSCAuqEEGpXGIbdIaGr1jfbRCUWsZ8SHkgA8GvI" alt="FlowChart" width="70%" />

</p>


- **재미요소**

사용자가 **다양한 조작법**과 **시각적인 재미요소**를 얻을 수 있도록 구상하여 구현함<br>
모티브를 받은 짱구 볼링게임에는 없는 기능들을 추가로 개발하였음 <br>
`joystick` 객체를 통해 사용자의 입력에 따라 볼링공이 직선으로 나가는지, 커브를 그리며 나가는지, 필살기 (짱구가 직접 굴러감)로 나가는지가 달라지도록 구현하였음 <br>


<p align="center">

<img src="https://github.com/classaen7/RaspberryPI_Bowling/blob/master/Assets/zzzanguskill1.png?raw=true" alt="필살기1" width="16%" />
<span style="display:inline-block; width:20px;"></span>
<img src="https://github.com/classaen7/RaspberryPI_Bowling/blob/master/Assets/zzzanguskill2.png?raw=true" alt="필살기2" width="16%" />
</p>




