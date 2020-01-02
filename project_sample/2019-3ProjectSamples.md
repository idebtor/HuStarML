# 19-3 프로젝트

## 넷플릭스 추천 시스템 알고리즘


휴스타 1기 ICT 특화 트랙에서 김영섭 교수님의 AI수업 프로젝트의 일환으로 하게된 프로젝트입니다.
이 노트는 아래 링크를 번역하고 수정하여 작성되었습니다.

https://www.kaggle.com/laowingkin/netflix-movie-recommendation 

Data set은
https://www.kaggle.com/netflix-inc/netflix-prize-data
에서 받을 수 있습니다.

이 프로젝트는 넷플릭스의 영화 추천 매커니즘을 만드는 것을 목표로 진행되었습니다. 넷플릭스가 Kaggle에 올린 dataset을 사용했고 여기엔 각각 약 4천개의 영화와 40만의 고객이 포함된 2000만개의 행을 가진 4개의 text data file이 있습니다. 따라서 모두 합하면 1만7천개의 영화와 50만이 넘는 고객의 리스트가 포함되어 있습니다.

약 2기가 쯤 되는 데이터를 커널에 로드하는 것부터 굉장한 도전이 됩니다. 따라서 원글의 작성자는 효율적인 데이터 접근을 하기위해 많은 노력을 했고 이는 코드에 나타나고 있습니다.


## 번호판 인식 (차량 번호판 인식기)

# 필요
- Python 3+
- pytesseract 4.0
- OpenCV
- numpy
- matplotlib

1. OCR 다운로드 및 설치
- https://github.com/tesseract-ocr/tesseract/wiki/4.0-with-LSTM#400-alpha-for-windows Windows Installer made with MinGW-w64 설치

  https://niceman.tistory.com/155 설치 방법

2.pip install opencv-python
3.pip install pytesseract

## FIFA 2019 데이터 분석 및 시각화
프로젝트를 하게 된 계기
평소 축구와 축구 게임에 관심이 많았는데, 실제 게임에서 어떤 항목을 가지고 선수들이 분류가 되는지, 그리고 얼마나 많은 데이터들이 축구 게임을 구성하는데 사용이 되는지 알고 싶어서 이 프로젝트를 하게 되었습니다.

다루게 될 Library
numpy

pandas

seaborn

matploblib

plotly

프로젝트개요
제공되어 있는 선수들의 데이터들을 이용해 시각화

각 나라별 Rating 분포
England가 가장 높을 것이라 예상했으나 많은 선수들 중 Rating이 높은 선수는 몇 안되서, 상대적으로 Spain과 France, Germany, Brazil, Argentina에 비해 현저히 낮은 Rating 분포가 나타났습니다.

## Generative Adversarial Networks을 이용한 사진 식별

1.	과제 계기
머신 러닝 관련 자료를 찾아보던 중, Generative Adversarial Networks(GAN)을 소개 받았습니다. 이는 생성적 적대 신경망으로 비지도 학습에 많이 사용되고 있으며, 제로섬 게임 틀 안에서 서로 경쟁하는 두개의 신경 네트워크 시스템에 의해서 구현됩니다.
여기서 제가 사용한 예제는 mnist 데이터를 이용해 인공 신경망이 mnist와 유사한 이미지를 만들기 위해 학습하며 이와 적대하는 인공 신경망은 mnist의 실제 데이터와 만들어진 데이터를 구분하기위한 학습을 하게 됩니다.

2.	과제 설명
여기엔 두가지의 학습 모델이 사용되고있는데
discriminator : Real데이터와 Fake데이터를 구분
generator : 랜덤한 코드를 통해 Discriminator에 적발되지않는 Fake데이터 생성
get_loss : discriminator 와 generator 손실함수


3.	결과
특별한 기준을 임의로 정해 준게 아니라 이 또한 인공 신경망을 통해 만들어진 판별 법이라 학습과정의 초기단계에서 학습 방향이 잘못 설정이 되버리면 판별 모델과 생성 모델 모두 망가지는 현상이 발생할 수 있습니다. 이 현상은 생성 모델의 기준이 판별 모델이 되어버려 생기는 현상인데, 모두 망가지지 않더라도 실제 데이터가 아닌 판별 모델을 기준으로 학습하는 특성상 궁극적인 목적인 실제 데이터와 유사한 데이터를 만들어내는 것이 어려울 수도 있습니다.

4.	참고
tensorflow 에 placeholder 가 없다는 오류 발생시
import tensorflow as tf 를
import tensorflow.compat.v1 as tf
tf.disable_v2_behavior() 로 대체 하세요.

## 데이터 분석을 통한 Scale불량 예측 모델링

1.	분석 배경
•	최근 제철소 후판 공정에서 Scale 불량이 급격히 증가하는 현상이 발생되었습니다. 해당 공정에서 추출된 데이터를 분석하여 불량의 원인을 찾고, 개선안을 도출하시오.
2.	개발환경
•	IDE
-	Jupyter notebook
•	프로그래밍 언어
-	Python
•	라이브러리
-	Pandas
-	numpy
-	matplotlib
-	seaborn
-	graphviz
-	sklearn
-	statsmodels
 
4.	기대효과
•	산업 현장에서 요구되는 문제 해결 능력을 배양하기 위해 실제 공정에서 발생되는 데이터와 유사한 데이터를 통해 인사이트를 도출해봄으로써 빅데이터 분석 실무 능력을 기른다.


## Word-level language modeling RNN

 선정이유
: 문장을 새로 만든다는게 신기해서 한번 해보고 싶었습니다.

 소개
------------
This example trains a multi-layer RNN (Elman, GRU, or LSTM) on a language modeling task. By default, the training script uses the Wikitext-2 dataset, provided. The trained model can then be used by the generate script to generate new text.

Conclusion
Dynamic quantization can be an easy way to reduce model size while only having a limited effect on accuracy.

Thanks for reading! As always, we welcome any feedback, so please create an issue here <https://github.com/pytorch/pytorch/issues>_ if you have any.


## 개와 고양이 사진 식별

프로젝트를 하게 된 계기

명사들의 강의를 보면 꼭 빠지지않고 딥러닝 발전의 예시로 개와 고양이를 구별하는 인공지능 소개가 나왔습니다. 그래서 이 프로젝트를 진행하면 딥러닝의 발전과정에 대한 좀 더 깊은 이해가 가능할거라 생각해 이 주제로 프로젝트를 진행했습니다.

 

다루게 될 기술

1. anaconda 

2. tensorflow

 

프로젝트개요

CNN 모델로 주어진 고양이와 개의 사진을 학습하여 새로운 사진이 주어졌을 때 주어진 사진이 개인지 고양이인지 구별할 수 있다.

1. 데이터 증식(Data argumentaion)

사진에 변형을 줌으로써 학습 데이터를 늘리고, 여러가지 변조에 강하게 모델을 학습시킬 수 있습니다.

2. CNN 모델 구성 및 학습

3. 학습결과 시각화 및 평가

4. 모델 중간 평가

5. 모델 예측


프로젝트 기대효과

딥러닝 진행과정을 경험하고 직접 해봄으로서 딥러닝에 대한 좀 더 깊은 이해가 가능하다.
































