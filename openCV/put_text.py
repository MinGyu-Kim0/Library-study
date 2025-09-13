import draw_diagram

import cv2
import numpy as np
import matplotlib.pyplot as plt

from PIL import Image
import requests
from io import BytesIO

# 텍스트 그리기 parameter. (좌 -> 우 순으로 입력받음)
# img, text - 표시할 문자열, org - 문자열이 표시될 위치. 문자열의 bottom-left corner 점
# fontFace - 폰트 타입(CV2.FONT_XXX), fontScale - 폰트 크기, color - 폰트 색상
# thichness - 글자의 굵기, lineType - 글자 선의 형태, bottomLeftOrigin - 영상의 원점 좌표 설정(True:최하단, False:좌상단)

img = draw_diagram.img
img = cv2.putText(img, 'OpenCV', (10, 500), cv2.FONT_HERSHEY_SCRIPT_SIMPLEX, 4, (255, 255, 255), 3)

plt.imshow(img)
plt.show