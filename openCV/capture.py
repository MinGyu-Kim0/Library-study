import cv2

# ret값, frame을 반환함(0은 웹캠의 번호)
cap=cv2.VideoCapture(0)

name = input()

while True:
    ret,frame=cap.read() # ret은 boolean값을 반환, frame은 화면 값
    if not ret:
        break

    # p를 ascii코드값으로 변경하여 입력받고 눌렀을때 출력중인 frame을 입력받았던 name변수값으로 저장
    cv2.imshow('Webcam',frame)
    if cv2.waitKey(1) == ord('p'):
        capture = cv2.imwrite(f'{name}.jpg', frame)
    
    # e를 누르면 사진 이름 변경
    if cv2.waitKey(1) == ord('e'):
        name = input()

    # q를 누르면 종료
    if cv2.waitKey(1) & 0xFF==ord('q'):
        break

cap.release()
cv2.destroyAllWindows()