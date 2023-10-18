import cv2
import numpy as np

# 카메라 장치 연결
cap = cv2.VideoCapture(0)

while cap.isOpened():
    # 프레임 읽기
    ret, frame = cap.read()

    # 속도 향상을 위해 영상 크기를 절반으로 축소
    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)

    if cv2.waitKey(1) == 27:  # ESC 키로 종료
        break

    # 컬러 이미지를 그레이 스케일로 변경
    gray_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    # 잡음 제거를 위해 가우시안 필터 적용 (라플라시안 필터 적용 전에 필요)
    gray_frame = cv2.GaussianBlur(gray_frame, (9, 9), 0)

    # 라플라시안 필터로 엣지 검출
    edges = cv2.Laplacian(gray_frame, -1, None, 5)

    # 스레시홀드로 경계 값만 남기고 제거하면서 화면 반전 (흰 바탕 검은 선)
    ret, sketch = cv2.threshold(edges, 70, 255, cv2.THRESH_BINARY_INV)

    # 경계선 강조를 위해 팽창 연산
    kernel = cv2.getStructuringElement(cv2.MORPH_CROSS, (3, 3))
    sketch = cv2.erode(sketch, kernel)

    # 경계선을 자연스럽게 하기 위해 미디언 블러 필터 적용
    sketch = cv2.medianBlur(sketch, 5)

    # 그레이 스케일에서 BGR 컬러 스케일로 변경
    img_sketch = cv2.cvtColor(sketch, cv2.COLOR_GRAY2BGR)

    # 컬러 이미지 선명도를 없애기 위해 평균 블러 필터 적용
    img_paint = cv2.blur(frame, (10, 10))

    # 컬러 영상과 스케치 영상과 합성
    img_paint = cv2.bitwise_and(img_paint, img_paint, mask=sketch)

    # 결과 이미지 합치기
    merged = np.hstack((img_sketch, img_paint))

    # 결과 출력
    cv2.imshow('Sketch Camera', merged)

# 카메라 연결 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
