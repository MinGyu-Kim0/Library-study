from ultralytics import YOLO
import cv2

model = YOLO("yolov8n.pt")

capture = cv2.VideoCapture(0)

x1 = 100
y1 = 100
x2 = 200
y2 = 200

while True:
    

    ret, frame = capture.read()
    roi = frame[y1:y2,x1:x2]
    results = model(roi)

    cv2.rectangle(frame, (100, 100), (200, 200), (0, 255, 0), 2)

    annotated = results[0].plot()

    frame[y1:y2, x1:x2] = annotated

    cv2.imshow("YOLOv8 Detection", frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

capture.release()
cv2.destroyAllWindows()

