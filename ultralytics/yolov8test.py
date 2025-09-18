from ultralytics import YOLO
import cv2


# 객체 인식을 위한 yolov8n 모델 사용
model = YOLO("yolov8n.pt")

# videocapture의 메소드 사용을 위해 class를 객체화
capture = cv2.VideoCapture(0)


# ROI 좌표 설정
x1 = 100
y1 = 100
x2 = 200
y2 = 200

# 카메라가 촬영가능 상태라면 반복문 실행
if capture.isOpened():
    while True:

        ret, frame = capture.read() # read는 boolean값과 이미지(넘파이배열)를 반환한다.
        roi = frame[y1:y2,x1:x2] # 모델에게 인식시킬 범위를 리스트 슬라이싱을 사용해 저장한다.
        
        # 잘라낸 이미지를 모델에 넘겨주고 모델은 추론 결과를 results로 반환한다.
        results = model(roi) # 이때 모델(yolo)은 박스 좌표, 클래스(class), 확률 정보등을 반환한다.

        # 모델에게 넘겨준 이미지 범위를 가시적으로 출력
        cv2.rectangle(frame, (100, 100), (200, 200), (0, 255, 0), 2)

        # 이미지에서 추론한 결과(results[0])를 전부(.plot()) annotated에 대입한다. roi이미지가 저장됨
        annotated = results[0].plot()

        # 탐지한 결과(annotated)를 다시 원본 프레임에 대입해서 영상에 보이도록 출력한다.
        frame[y1:y2, x1:x2] = annotated

        # 윈도우 창의 이름을 설정하고 어떤 화면을 송출할지 정해준다.
        cv2.imshow("YOLOv8 Detection", frame)

        # 키 입력을 기다리고 q가 입력되면 반복문 탈출
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

# 화면 닫기
capture.release()
cv2.destroyAllWindows()

