# 이미지 읽기
import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
import requests
from io import BytesIO

url = 'https://cdn.pixabay.com/photo/2025/08/21/09/51/rouen-cathedral-9787080_1280.jpg'

response = requests.get(url)

# PIL.Image - 사진 파일을 다루는 객체
# 픽셀 값은 들어 있으나 직접 수치를 연산하기에 적절하지 않음.
pic = Image.open(BytesIO(response.content))

print(type(pic))

# 이미지 출력(PIL)

# pic변수에 저장된 PIL.Image 객체를 numpy 배열로 변환.
# 수치에 접근하기 위해서(ex: 그래프창에 사진 출력하기) 아래와 같이 numpy 배열로 변환하여 접근한다.
pic_arr = np.asarray(pic)
print(type(pic_arr)) # type = numpy.ndarray

print(pic_arr.shape)

print(pic_arr) # (1280, 854, 3), (세로, 가로, 차원 개수(R, G ,B 3))

# 이미지 출력(matplotlib)

plt.imshow(pic_arr) # 이미지를 배열 형태로 받아서 '그래프' 창에 그려준다.
plt.show() # 지금까지 준비된 그래프/그림을 화면에 띄운다.

pic_copy = pic_arr.copy()

plt.imshow(pic_copy)
plt.show()

print(pic_copy.shape)

print(pic_copy[:, :, 0]) # red 차원만 볼 수 있게 설정. 2차원 정보만 출력
print(pic_copy[:, :, 0].shape)

plt.imshow(pic_copy[:, :, 0])
plt.show() 

plt.imshow(pic_copy[:, :, 0], cmap='gray')
# plt.show()

pic_red = pic_arr.copy()
pic_red[:, :, 1] = 0 # red 제외 모든 값을 0으로 만들어 이미지 출력
pic_red[:, :, 2] = 0
print(pic_red)
plt.imshow(pic_red)
plt.show()

pic_green = pic_arr.copy()
pic_green[:, :, 0] = 0 # green 제외 모든 값을 0으로 만들어 이미지 출력
pic_green[:, :, 2] = 0
print(pic_green)
plt.imshow(pic_green)
plt.show()

pic_blue = pic_arr.copy()
pic_blue[:, :, 0] = 0 # blue 제외 모든 값을 0으로 만들어 이미지 출력
pic_blue[:, :, 1] = 0
print(pic_blue)
plt.imshow(pic_blue)
plt.show()

# 이미지 출력 (OpenCV)

cv2.imshow("test", pic_arr) # 이미지를 OS에서 제공하는 '윈도우 창'을 열어서 출력한다.
cv2.waitKey(0)           # 키 입력 대기 (0이면 무한 대기)
cv2.destroyAllWindows()

# OpenCV는 BGR순으로 나타내기 때문에 RGB순으로 뒤집는 method를 지원하고 이를 사용함.
image = cv2.cvtColor(pic_arr, cv2.COLOR_RGB2BGR)

cv2.imshow("test2", image)
cv2.waitKey(0)        
cv2.destroyAllWindows()

print(image[0][0]) # OpenCV는 BGR 순으로 읽기 때문에 역순으로 보임
print(pic_arr[0][0]) # RGB 순

temp_arr = pic_arr[:, :, ::-1] # 리스트 슬라이싱으로 BGR -> RGB 순으로 바꾸기
print(pic_arr[0][0]) # BGR
print(temp_arr[0][0]) # RGB 