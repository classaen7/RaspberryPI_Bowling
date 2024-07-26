# Raspberry Pi를 이용한 파이썬 게임 프로젝트 (개인 프로젝트)


<p align="center">

<img src="https://github.com/user-attachments/assets/f375d82b-366e-4748-8a79-afbd6cb58ba7" alt="라즈베리파이 로고" width="12%" />
</p>

임베디드 SW를 공부하면서 라즈베리파이로 게임을 만드는 프로젝트를 하게 되었다. <br>
이 프로젝트를 통해 **객체지향 프로그래밍 기법**과 **파이썬 이미지 처리**에 대한 실력을 늘리고 싶었다. <br>
또한 **시각적으로 흥미**를 끌만한 게임을 만들고 싶었다. <br>
어렸을 때 플래시 게임으로 짱구 볼링게임을 한적이있는데, 이를 모티브로 하여 추가적인 재미요소 또한 구현하기로 하였다. 

## Preview

<p align="center">
 
<img src="https://github.com/user-attachments/assets/dad482c5-3421-4d70-bf1b-edd89d89628e">

</p>

<p style="text-align: center;">
 
🎞️ [전체 플레이 영상](https://www.youtube.com/watch?v=o6zWwLnBUOc)

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
<img src="https://github.com/user-attachments/assets/35bd5c53-5600-4e8a-abd2-e8e00324f73d" alt="FlowChart" width="70%" />

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




