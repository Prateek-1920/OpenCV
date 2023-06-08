import cv2 as cv
import numpy as np
import imutils
import cvzone

vid = cv.VideoCapture(0)
while True:
    ret, frame = vid.read()
    if not ret:
        break

    # BLURRING
    blur = cv.GaussianBlur(frame, (9, 9), 0)
    blurred = cv.medianBlur(blur, 9, 0)

    # HSV CONVERSION
    hsv = cv.cvtColor(blurred, cv.COLOR_BGR2HSV)

    lower = (25, 50, 70)
    upper = (35, 255, 255)

    mask = cv.inRange(hsv, lower, upper)
    mask = cv.erode(mask, None, iterations=2)
    mask = cv.dilate(mask, None, iterations=3)

    contours = cv.findContours(mask.copy(), cv.RETR_EXTERNAL,
                               cv.CHAIN_APPROX_SIMPLE)
    contours = imutils.grab_contours(contours)
    center = None

    if len(contours) > 0:
        c = max(contours, key=cv.contourArea)
        ((x, y), radius) = cv.minEnclosingCircle(c)
        centroid = cv.moments(c)
        center = (int(centroid["m10"] / centroid["m00"]),
                  int(centroid["m01"] / centroid["m00"]))
        # only proceed if the radius meets a minimum size
        if radius > 15:
            cv.circle(frame, (int(x), int(y)), int(radius),
                      (0, 255, 255), 2)
            cv.circle(frame, center, 5, (0, 0, 255), -1)

    stacked = cvzone.stackImages([frame, hsv, mask], 3, 1)
    cv.imshow("Ball", stacked)

    # cv.imshow("Vid", frame)
    # cv.imshow("hsv", hsv)
    # cv.imshow("mask", mask)

    if cv.waitKey(1) & 0xFF == ord('q'):
        break

vid.release()
cv.destroyAllWindows()
