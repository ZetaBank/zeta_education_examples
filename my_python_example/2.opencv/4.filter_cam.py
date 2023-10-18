import cv2
import numpy as np

# 웹캠 비디오 캡처 객체 생성
cap = cv2.VideoCapture(0)

# 캡처된 비디오 프레임 크기 설정
cap.set(cv2.CAP_PROP_FRAME_WIDTH, 320)
cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 240)

# 프레임의 행(row)과 열(column) 크기 설정
frame_height, frame_width = 240, 320

# 거울 왜곡 효과를 위한 좌표 매핑 생성
map_y, map_x = np.indices((frame_height, frame_width), dtype=np.float32)

# 좌우 대칭 거울 좌표 연산
map_mirror_horizontal_x, map_mirror_horizontal_y = map_x.copy(), map_y.copy()
map_mirror_horizontal_x[:, frame_width // 2:] = frame_width - map_mirror_horizontal_x[:, frame_width // 2:] - 1

# 상하 대칭 거울 좌표 연산
map_mirror_vertical_x, map_mirror_vertical_y = map_x.copy(), map_y.copy()
map_mirror_vertical_y[frame_height // 2:, :] = frame_height - map_mirror_vertical_y[frame_height // 2:, :] - 1

# 물결 효과를 위한 좌표 매핑 생성
map_wave_x, map_wave_y = map_x.copy(), map_y.copy()
map_wave_x = map_wave_x + 15 * np.sin(map_y / 20)
map_wave_y = map_wave_y + 15 * np.sin(map_x / 20)

# 렌즈 효과를 위한 좌표 매핑 생성
map_lens_x = 2 * map_x / (frame_width - 1) - 1
map_lens_y = 2 * map_y / (frame_height - 1) - 1

# 렌즈 효과, 극좌표 변환
r, theta = cv2.cartToPolar(map_lens_x, map_lens_y)
r_convex = r.copy()
r_concave = r

# 볼록 렌즈 효과 매핑 좌표 연산
r_convex[r < 1] = r_convex[r < 1] ** 2

# 오목 렌즈 효과 매핑 좌표 연산
r_concave[r < 1] = r_concave[r < 1] ** 0.5

# 렌즈 효과, 직교 좌표 복원
map_convex_x, map_convex_y = cv2.polarToCart(r_convex, theta)
map_concave_x, map_concave_y = cv2.polarToCart(r_concave, theta)

# 렌즈 효과, 좌상단 좌표 복원
map_convex_x = ((map_convex_x + 1) * frame_width - 1) / 2
map_convex_y = ((map_convex_y + 1) * frame_height - 1) / 2
map_concave_x = ((map_concave_x + 1) * frame_width - 1) / 2
map_concave_y = ((map_concave_y + 1) * frame_height - 1) / 2

while True:
    # 비디오 프레임 읽기
    ret, frame = cap.read()

    # 준비한 매핑 좌표로 영상 효과 적용
    mirror_horizontal = cv2.remap(frame, map_mirror_horizontal_x, map_mirror_horizontal_y, cv2.INTER_LINEAR)
    mirror_vertical = cv2.remap(frame, map_mirror_vertical_x, map_mirror_vertical_y, cv2.INTER_LINEAR)
    wave = cv2.remap(frame, map_wave_x, map_wave_y, cv2.INTER_LINEAR, None, cv2.BORDER_REPLICATE)
    convex_lens = cv2.remap(frame, map_convex_x, map_convex_y, cv2.INTER_LINEAR)
    concave_lens = cv2.remap(frame, map_concave_x, map_concave_y, cv2.INTER_LINEAR)

    # 영상 합치기
    top_row = np.hstack((frame, mirror_horizontal, mirror_vertical))
    bottom_row = np.hstack((wave, convex_lens, concave_lens))
    merged_frame = np.vstack((top_row, bottom_row))

    # 결과 영상 출력
    cv2.imshow('Distorted Effects', merged_frame)

    # ESC 키를 누르면 루프 종료
    if cv2.waitKey(1) & 0xFF == 27:
        break

# 비디오 캡처 객체 해제 및 창 닫기
cap.release()
cv2.destroyAllWindows()
