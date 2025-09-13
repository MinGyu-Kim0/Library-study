import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
import requests
from io import BytesIO

img = np.zeros((512, 512, 3), np.uint8)

# plt.imshow(img)
# plt.show() # 검은색 사각형 출력

# 직선 그리기
# img - 그림을 그릴 이미지 파일, start - 시작 좌표, end - 종료 좌표
# color - RGB형태의 Color(e.g.,(255,0,0) -> Red), thickness(int) 선의 두께(pixel)

img = cv2.line(img, (0, 0), (511, 511), (255, 0, 0), 5)
# plt.imshow(img)
# plt.show()

# 사각형 그리기

img = cv2.rectangle(img, (300, 0), (510, 128), (0, 255, 0), 5)
# plt.imshow(img)
# plt.show()

# 원 그리기
# img, center 원의 중심 좌표(x, y), radian - 반지름, color - RGB형태의 Color, thickness - 선 두께, -1이면 원 안쪽을 채움
# lineType - 선의 형태, cv2.line()함수의 인수와 동일, shift 좌표에 대한 비트 시프트 연산

img = cv2.circle(img, (450, 50), 50, (0, 0, 255), -1)
# plt.imshow(img)
# plt.show()

img = cv2.circle(img, (50, 450), 50, (0, 255, 255), 2)
# plt.imshow(img)
# plt.show()

# 타원 그리기
# img, center, axes - 중심에서 가장 큰 거리와 작은 거리, angle - 타원의 기울기 각
# startAngle - 타원의 시작 각도, endAngle - 끝나는 각도, color, thickness, lineType, shift

img = cv2.ellipse(img, (256, 256), (150, 30), 0, 0, 180, (0, 255, 0), -1)
# plt.imshow(img)
# plt.show()

img = cv2.ellipse(img, (256, 256), (150, 50), 45, 0, 360, (255, 255, 255), 2)

img = cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 4, (255, 255, 255), 3)

plt.imshow(img)
plt.show()
