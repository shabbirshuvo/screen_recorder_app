import cv2
img = cv2.imread('./images/face1.png', 0)
# 0 is grayscale, 1 is color, -1 is unchanged
img = cv2.line(img, (0, 0), (255, 255), (255, 0, 0), 5)
# 0, 0 is the starting point, 255, 255 is the ending point, (255, 0, 0) is the color, 5 is the thickness
# draw a line on the image

img = cv2.arrowedLine(img, (0, 255), (255, 255), (0, 255, 0), 5)
# draw an arrowed line on the image

img = cv2.rectangle(img, (100, 0), (150, 200), (0, 0, 255), -1)
# draw a rectangle on the image
# -1 is the thickness, if it is -1, the rectangle will be filled with the color
# if it is 0, the rectangle will not be drawn
# if it is 1 or any other number, the rectangle will be drawn with the thickness of that number

img = cv2.circle(img, (200, 200), 50, (255, 255, 0), -1)
img = cv2.circle(img, (200, 200), 100, (0, 255, 100), 5)
img = cv2.putText(img, "This is awesome", (50, 100), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 0, 255), 10, cv2.LINE_AA)

cv2.imshow('image', img)

key = cv2.waitKey(0)
# 0 is infinite, the window will not close until you press any key
if key == 27:
    cv2.destroyAllWindows()
elif key == ord('s'):
    cv2.imwrite('./images/face1_gray1.png', img)
    cv2.destroyAllWindows()

# cv2.waitKey(5000)
# 0 is infinite, the window will not close until you press any key
# 5000 is 5 seconds, the window will close after 5 seconds

# cv2.imwrite('./images/face1_gray.png', img)

cv2.destroyAllWindows()

