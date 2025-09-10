import cv2
import numpy as np
import matplotlib.pyplot as plt

# Python Imaging Library - PIL
# 다양한 이미지 포맷을 파이썬 객체로 열고, 변환, 저장, 처리 가능
from PIL import Image 

# HTTP 통신을 위한 라이브러리
import requests

# BytesIO - 바이트 데이터를 파일처럼 다룰 수 있게 해주는 객체
from io import BytesIO

url = 'https://cdn.pixabay.com/photo/2018/08/09/15/31/lion-3594781_640.jpg'

# url로부터 데이터를 다운로드(이미지 또한 0과1로 이루어진 바이너리 데이터이므로)
response = requests.get(url) 
pic = Image.open(BytesIO(response.content)) # PIL을 사용해 이미지 객체화

pic_np = np.array(pic) # 이미지 출력을 위해 배열 값(numpy)으로 변환

pic_bgr = cv2.cvtColor(pic_np, cv2.COLOR_RGB2BGR) # RGB -> BGR

# cv2.imshow("Lion", pic_bgr)
# cv2.waitKey(0)
# cv2.destroyAllWindows

# plt.imshow(pic_bgr)
# plt.show()

img_gray = cv2.cvtColor(pic_np, cv2.COLOR_BGR2GRAY)
print(img_gray.shape) # (640, 456) grayScale이 되어 2차원 배열로 출력

# cv2.imshow("Lion", img_gray)
# cv2.waitKey(0)
# cv2.destroyAllWindows

# # plt로 출력하는 경우 gray로 명시를 해주어야 함. default = color
# plt.imshow(img_gray, cmap='gray') # 외에도 magma 등등이 있음.
# plt.show()

# cv2.imwrite() 경로, 이미지 배열을 인자로 받음

# 랜덤한 값으로 가상의 이미지 생성. dtype(data type),np(numpy), uint(unsigned int), 8(bit)
random_image = np.random.randint(0, 256, size=(200, 200, 3), dtype=np.uint8)
print(random_image.shape) # ( 200, 200, 3 )

# 이미지 저장을 하면 True반환
# 없는 이미지를 읽어도 type이 NoneType으로 들어갈 뿐 에러를 발생하지 않음
print(cv2.imwrite('random_image.png', random_image))

cv2.imshow("random", random_image)
cv2.waitKey(0)
cv2.destroyAllWindows