import cv2
import numpy as np
import pyautogui

# img = pyautogui.screenshot()
# img.save("test_screenshot.png")


record_button = None
# fourcc = cv2.VideoWriter_fourcc(*'XVID')
# output_file = 'screen_record.avi'
fourcc = cv2.VideoWriter_fourcc(*'mp4v')
output_file = 'screen_record.avi'

fps = 30.0
out = None
screen_size = (int(pyautogui.size().width), int(pyautogui.size().height))
recording = False

print(screen_size)
print(type(screen_size))
print(fourcc)

for i in range(1000):   #
    out = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'XVID'), fps, screen_size)
    img = pyautogui.screenshot()
    frame = np.array(img)
    frame = cv2.cvtColor(frame, cv2.COLOR_RGB2BGR)
    out.write(frame)
out.release()
# cv2.imwrite("test_frame.png", frame)
