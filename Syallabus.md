# HuStar Robot Academy - AI for Robot Course

#### By Youngsup Kim, idebtor@gmail.com, Handong Global University
-------------------------------
### How to view markdown(.md) files in Chrome (or rendering in HTML)
 0. View them in github website automatically.
 and/or
 1. Install `markdown preview plus` extension.
 2. Check the option `Allow access to file URLs` in `chrome://extensions -> markdown preview plus` listing.
    (크롬에서 `chrome://extensions` 접속 한 후, `markdown preview plus` `세부정보`에서 "파일 URL에 대한 액세스 허용"을 체크하십시오)
 3. Open local or remote .md file in Chrome.
 4. Enjoy nicely formatted HTML!

## 들어가면서

“자율로봇 인공지능” 과목을 소개합니다.

세상은 인공지능으로 인하여 상당히 큰 변화를 맞이하고 있는데, 마치 거대한 파도가 온 세상을 덮치며 세상을 변화시킬 듯합니다. 최근에 자주 듣는 소식 중에 하나만 예로 들자면 “무인화”입니다. 편의점, 주유소, 교통, 유통, 제조, 금융에 이르기까지 상당히 많은 분야에서 일어나고 있는 무인화의 핵심 기술은 인공지능 혹은 기계학습(딥러닝)이라고 부릅니다. 기계들이 학습을 통해 지능을 갖추면서 인간 노동을 상당부분 대체하기 시작한 것입니다.  미국의 아마존 고, 중국의 빙고박스, 알리바바의 타오카페 등 거대한 IT기업과 유통 기업들이 폭발적으로 무인 점포를 늘리고 있다는 소식입니다. 예전에는 아마존과 알리바바 직원들이 하루 평균 20 Km를 걸어 다니며 주문된 상품을 찾았다고 하는데, 이제는 물류 자율로봇 [Kiva](https://www.youtube.com/watch?v=UTNsaG5ZleE)가 이 일을 모두 감당합니다.  2000년대 초에 골드만 삭스에 있던 600명의 트레이더들이 인공지능 [Kensho](https://newspeppermint.com/2016/03/24/kensho3/)로 말미암아 결국은 4명으로 감원되었습니다.  
스탠포드 앤드류 응 교수는 [“Artificial Intelligence is the New Electricity"](https://www.youtube.com/watch?v=NQK4ZY_gwKI)라고 말합니다.  전기의 발명으로 2차 산업혁명이 있었던 것처럼, 우리 앞에 다가온 4차혁명의 핵심에 있는 것이 바로 인공지능이며, 인공지능의 근간을 이루는 것이 기계학습 곧 딥러닝입니다. 이런 기술이 기존의 산업과 융합하면서 금융, 교육, 의료, 유통, 교통 등 전 산업에 걸쳐 그야말로 파괴적 혁신을 주도하고 있습니다.  우리가 바로 이러한 기술의 핵심을 이제 도전해 보려는 것입니다.
최근에는 다양한 채널을 통해 탁월한 인공지능 강의를 얼마든지 접할 수 있습니다. 하지만 그런 훌륭한 강의도 수학적 지식을 바탕으로 한 이론에만 치중하거나, 복잡한 프로그래밍을 할 수 있는 전공자들을 대상으로 한다거나, 아니면 추상적인 강의들이 많습니다. 그러나, 이번 HuStar 아카데미의 자율로봇 인공지능 강의는 세가지에 초점을 맞추고 있습니다. 첫째는 인공지능에 활용할 때 필수적으로 사용해야 하는 파이썬 프로그래밍의 기본을 학습하고, 둘째는 이를 이용하여 인공지능의 원리를 이해하고, 그 원리를 적용할 수 있는 문제(프로젝트)를 경험하여, 결국에는 HuStar Academy에서 추구하는 자율로봇에도 적용할 수 있는 역량을 키우려고 합니다.
본 과목을 자동차로 비유하자면, 자동차 엔진이나 자동차를 개발하는 과정이 아니라, 인공지능이라는 자동차를 직접 운전해보는 경험을 맛볼 수 있도록 하는 과정입니다. 자동차 운전을 배우면서, 그 자동차로 무엇을 할 수 있는지 탐색하고, 혹은 운전 자체를 잘 하려면 어떻게 해야 하는지, 혹은 이미 존재하는 다양한 자동차들로 어떤 다양한 일을 할 수 있는지, 혹은 더 좋은 자동차를 만들려면 무엇을 해야 하는지 알 수 있도록 “인공지능 자동차”를 한번 경험해보도록 하는 과정이라고 비유할 수 있습니다. 인공지능으로 할 수 있는 사례들을 찾아서 자신이 인공지능을 직접 적용할 수 있는 문제를 발굴하고 도전해 볼 수 있는 학습 능력을 갖추도록 하는 것을 목적으로 진행합니다.  

(전산전자공학부 김영섭 교수)

## 1.	학습목표 (Course Objective)
 - 인공지능의 기본 원리를 이해한다
 - 파이썬과 넘파이 코딩 역량을 갖춘다
 - 인공지능 프로젝트 수행 역량을 갖춘다

## 2.	강의 개요(Course Description)
4차 산업 혁명 시대에 핵심 기술은 인공지능입니다. 어떤 분야이든지 앞으로는 누구나 인공지능에 대한 지식은 필수적입니다. 이를 위해서 HuStar 수강생들이면 누구나 인공지능에 접근 할 수 있도록 수업을 구성하였습니다.  먼저 인공지능에 관련 개념을 이해하고, 인공지능 프로젝트를 들어가기 전 필요한 파이썬 코딩을 배울 것입니다.  인공지능 알고리즘을 공부하고 직접 작동해 보면서 인공지능이 어떻게 동작하는지 이해하는 시간을 가질 것입니다.

본 과정은 어렵고 복잡한 인공지능을 수강생들이 접근 가능하도록 도와주는 것을 목표로 합니다. 본 과정을 통해, 인공지능에 대한 개념과 기술을 이해하고, 이러한 기술을 적용하기 위해 필요한 파이썬 코딩을 배우고, 마지막으로 이를 문제해결을 위해 실제적으로 적용하는 프로젝트를 경험해 볼 것입니다. 그렇게 함으로 본 과정에서 공부한 것을 바탕으로 HuStar에서 최종 목표로 하는 자율 로봇에도 인공지능을 적용할 수 있는 문제해결 역량을 키우는 것이 목적입니다.

## 3. 강의 일정 계획(Daily Schedule)

### 1일차
1. 인공지능으로의 초대(1)
  - [Kiva](https://www.youtube.com/watch?v=UTNsaG5ZleE)
  - [Kensho](https://newspeppermint.com/2016/03/24/kensho3/)
  - [“Artificial Intelligence is the New Electricity"](https://www.youtube.com/watch?v=NQK4ZY_gwKI)

  - KMOOCx 강의 1-1, 1-2, 1-3   
		- 1-1 (https://www.youtube.com/watch?v=cvfxrxhy9KA)   
		- 1-2 (https://www.youtube.com/watch?v=PrJ3bgit620)   
		- 1-3 (https://www.youtube.com/watch?v=D2Y60uJY_o0)   
	- KMOOCx 퀴즈 1-1, 1-2, 1-3   
		- [Quiz 1-1] (https://docs.google.com/forms/d/e/1FAIpQLSd2Y4RzIehedgF4hESw5y72P0r_sLckm101gbCJENrjhzImAQ/viewform?usp=sf_link)
		- [Quiz 1-2] (https://docs.google.com/forms/d/e/1FAIpQLSfDbWRa7ayCEuqynaJHXkhkK6sM3jkt4vlIMzMeVgLWTRZbMg/viewform?usp=sf_link)
		- [Quiz 1-3] (https://docs.google.com/forms/d/e/1FAIpQLSctzapSilQq8togt4YSNReNLgWhhUdKik1jvTsDB7wa4F_R0g/viewform?usp=sf_link)
  - 명강의 시리즈(1)
    - [남세동의 인공지능(딥러닝) 이야기 (8분)](https://www.youtube.com/watch?v=kMGEpIYPCiM)
    - [How computers learn to recognize objects instantly (8분)](https://www.youtube.com/watch?v=Cgxsv1riJhI&t=208s)
    - [Quiz 1](https://forms.gle/jHUNTED9A4fRq75z6)

1. Python&AI 코딩으로의 초대(1)
  - 인공지능 개발환경 구축
    - AI1-1 Gettingstarted.ipynb
    - AI1-2 Jupyter.ipynb
    - AI1-3 Markdown.ipynb
      - Git, GitHub, Github Desktop
        [동영상 강의](https://www.youtube.com/watch?v=WPt3fhljd-c&list=PLQS78DCab0Iptq84l3_x_DTpzfwthj1Mh&index=3)
      - Anaconda (Python Development Package)
      - Jupyter-Lab (or Jupyter Notebook)
        [동영상 강의](https://www.youtube.com/watch?v=LJTjViQ87VM&list=PLQS78DCab0Iptq84l3_x_DTpzfwthj1Mh&index=2)  
  -	Jupyter/Py1 Overview.ipynb  
  - Jupyter/Py2 DataTypes.ipynb  

### 2일차
2. 인공지능으로의 초대(2)
  - KMOOCx 강의 2-1, 2-2, 2-3
	 - 2-1 (https://www.youtube.com/watch?v=kFBno_BQ2g4)
	 - 2-2 (https://www.youtube.com/watch?v=YH9dEQ6NwF8)
	 - 2-3 (https://www.youtube.com/watch?v=6NsyPodmSBk)
	- KMOOCx 퀴즈 2-1, 2-2, 2-3
	 - [Quiz 2-1] (https://docs.google.com/forms/d/e/1FAIpQLSfK2C6FStV7RttyAPXqhlULxuwWJ6H6HOGB6O7p7RLNrYVxSQ/viewform?usp=sf_link)
	 - [Quiz 2-2] (https://docs.google.com/forms/d/e/1FAIpQLSfA47mSxS4ccMEtpQ4CqXLqMKuW8NcxcClCePlAfXEHOUUmXg/viewform?usp=sf_link)
	 - [Quiz 2-3] (https://docs.google.com/forms/d/e/1FAIpQLScxAKljNI3O1k282qXF7RAwy3WXW4dI-p-wPU30Eyu84fD-Zg/viewform?usp=sf_link)
  - 명강의 시리즈(2)
    - [머신러닝, 딥러닝 초간단 설명(7분)](https://www.youtube.com/watch?v=aF03asAmQbY)
    - [인공지능의 주인이 되기 위해 반드시 알아야 할 것들 (15분)](https://youtu.be/BKj3fnPSUIQ)
    - [Fake videos of real people -- and how to spot them(7분)](https://youtu.be/o2DDU4g0PRo)
    - [Quiz 2](https://forms.gle/wh6u11F3dCJtjNei6)

2. Python&AI 코딩으로의 초대(2)
  - Jupyter/Py3 Iteration.ipynb
  - Jupyter/Py4 Function.ipynb
  - Jupyter/AI4-1 LinearRegression.ipynb

### 3일차
3. 인공지능으로의 초대(3)
  - KMOOCx 강의 3-1, 3-2, 3-3
	 - 3-1
	 - 3-2
	 - 3-3
  - 명강의 시리즈(3)
    - [How we teach computers to understand pictures (17분45초)](https://youtu.be/40riCqvRoMs)
    - [How AI can save our humanity (15분)](https://youtu.be/ajGgd9Ld-Wc)
    - [Quiz 3](https://forms.gle/53TCeUh18Uf7QsP9A)

3. Python&AI 코딩으로의 초대(3)
  - Jupyter/Py5 String.ipynb
  - Jupyter/Py6 List.ipynb
  - Jupyter/AI4-2 GradientDescent.ipynb

### 4일차
4. 인공지능으로의 초대
  - KMOOCx 강의 
    - 4-1
    - 4-2 
    - 4-3
  - 명강의 시리즈(4)
    - [The incredible inventions of intuitive AI(15분23초)](https://www.youtube.com/watch?v=aR5N2Jl8k14)
    - [How a Driverless Car sees the Road(15분)](https://youtu.be/tiwVMrTLUWg)
    - [Quiz 4](https://forms.gle/8mqRf7GFU7L1EzHy6)

4. Python&AI 코딩으로의 초대(4)
  - Jupyter/Py7 Listcomp.ipynb
  - Jupyter/Py8 Dictionary.ipynb
  - Jupyter/AI4-3 LossFunction.ipynb

### 5일차
5. 인공지능으로의 초대
  - KMOOCx 강의 
    - 5-1
    - 5-2
    - 5-3
  - 명강의 시리즈(5)
    - [How we can teach computers to make sense of our emotions 11분13초](https://youtu.be/hs-YuHv0vUk)
    - [Can a robot pass a university entrance exam? 13분37초](https://www.youtube.com/watch?v=BXcFEhl7ynM)
    - [Quiz 5](https://forms.gle/ntdB6N8DMBTFtxkVA)
  
4. Python&AI 코딩으로의 초대(5)
  - Jupyter/AI3-1 NumPyBasics.ipynb
  - Jupyter/AI3-2 NumPyArrays.ipynb
  - Jupyter/AI3-3 NumPySlicing.ipynb
  - Jupyter/AI4-4 NeuronClass.ipynb

### 6일차
6. 인공지능으로의 초대
  - KMOOCx 강의 6-1, 6-2, 6-3
  - 명강의 시리즈(6)
    - [적정선은 어디인가? How Far is Too Far - 34분39초](https://youtu.be/UwsrzCVZAb8)
    - [Quiz 6](https://forms.gle/j4NQcbWcscKGByEs6)


6. 내 손으로 만져보는 인공지능(1)
  - 인공지능의 동작 원리,
  - 퍼셉트론, 다중 퍼셉트론, OOP 퍼셉트론
  - 선형 회귀, 경사 하강법

6. Python&AI 코딩으로의 초대(6)
  - Jupyter/AI3-4 NumPyBroadcast.ipynb
  - Jupyter/AI3-5 NumPyRandom.ipynb
  - Jupyter/AI3-6 NumPyProblemSet.ipynb
  - Jupyter/AI5-1 Perceptron_Sigmoid.ipynb

### 7일차
7. 인공지능으로의 초대
  - KMOOCx 강의 7-1, 7-2, 7-3
  - 명강의 시리즈(7)
    - [A.I.를 통한 치유(Healed through A.I.) - 39분54초](https://youtu.be/V5aZjsWM2wo)
    - [Quiz 7](https://forms.gle/DpKTcUmv6TgNTdw46)
  
  
7. Python&AI 코딩으로의 초대(7)  
  - Jupyter/AI7-1 Gate Final.ipynb6. 
  - Jupyter/AI7-2 XOR.tf.keras Final.ipynb
  - Jupyter/AI7-3 MNIST.tf.keras Final.ipynb

7. 내 손으로 만져보는 인공지능(2)
  - 로지스틱 회귀, 손실함수
  - MNIST자료 이해
  - 순전파 MNIST

### 8 ~ 10일차:
내 손으로 만져보는 인공지능 및 프로젝트 수행과 발표
8. 내 손으로 만져보는 인공지능(3)
  - 오차 역전파, 모델 만들기
  - 역전파 MNIST

9. 내 손으로 만져보는 인공지능(4)
  - 배추가격 예측하기
  - 한동대 재학생 인공지능 프로젝트 내 것으로 만들기   

10. 내 손으로 만져보는 인공지능(5)
  - MNIST 손글씨 숫자 인식하기(그룹 프로젝트)   
  - 내가 찾아낸 인공지능(그룹 프로젝트)

### 본 교과목은 위의 영역에서 각 1개 이상의 프로젝트 수행하는 것을 목표로 함
------------------------------------------
_In the beginning, God created the heaven and the earth. Gen1:1_
