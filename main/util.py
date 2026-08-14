import numpy as np

def get_angle(a,b,c):
    #tính góc giữa vector BA và BC, chuẩn hóa về khoảng [0, 180] độ
    radian = np.arctan2(c[1] - b[1], c[0] - b[0]) - np.arctan2(a[1] - b[1],a[0] - b[0])
    angle = np.abs(np.degrees(radian))
    
    angle = angle % 360
    if angle > 180:
        angle = 360 - angle
    return angle

def get_distance(landmarks_list):
    #tính khoảng cách Euclidean và nhân hệ số 1000 để làm việc với số nguyên
    if len(landmarks_list) < 2:
        return
    
    (x1,y1),(x2,y2) = landmarks_list[0],landmarks_list[1]
    L = np.hypot(x2 - x1,y2 - y1)
    return L * 1000


