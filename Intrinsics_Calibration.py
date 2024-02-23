import numpy as np
import cv2

CHECKERBOARD_SIZE = (8,6)  # Change this to match your checkerboard size(inner corners)

objp = np.zeros((CHECKERBOARD_SIZE[0]*CHECKERBOARD_SIZE[1], 3), np.float32)
objp[:, :2] = np.mgrid[0:CHECKERBOARD_SIZE[0], 0:CHECKERBOARD_SIZE[1]].T.reshape(-1, 2)

obj_points = []  # 3d points in real world space
img_points = []  # 2d points in image plane

images = [f"Calibration_Images/Intrinsics/calibration{i}.jpg"for i in range(6,11)]
t=0
for fname in images:
    img = cv2.imread(fname)
    gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
    # Find the chessboard corners
    ret, corners = cv2.findChessboardCorners(gray, CHECKERBOARD_SIZE, None)

    # If found, add object points, image points (after refining them)
    if ret:
        obj_points.append(objp)
        print("ok")
        corners2 = cv2.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria=(cv2.TERM_CRITERIA_EPS + cv2.TERM_CRITERIA_MAX_ITER, 30, 0.001))
        img_points.append(corners2)

        # Draw and display the corners
        img = cv2.drawChessboardCorners(img, CHECKERBOARD_SIZE, corners2, ret)
        cv2.imwrite(f'calibresult{t}.png', img)
        t+=1

# Perform camera calibration
ret, mtx, dist, rvecs, tvecs = cv2.calibrateCamera(obj_points, img_points, gray.shape[::-1], None, None)

print("Calibration successful. Calibration matrix (mtx):\n", mtx)
print("Distortion coefficients (dist):\n", dist)

new_img = cv2.imread('Calibration_Images/Intrinsics/calibration6.jpg')
h,  w = new_img.shape[:2]
newcameramtx, roi = cv2.getOptimalNewCameraMatrix(mtx, dist, (w,h), 1, (w,h))

mapx, mapy = cv2.initUndistortRectifyMap(mtx, dist, None, newcameramtx, (w,h), 5)
dst = cv2.remap(new_img, mapx, mapy, cv2.INTER_LINEAR)

# crop the image
x, y, w, h = roi
dst = dst[y:y+h, x:x+w]
cv2.imwrite('calibresult.png', dst)