import cv2
import datetime

# Open the default camera
video_capture = cv2.VideoCapture(0)

# Check if the camera opened successfully
if not video_capture.isOpened():
    print("Error: Could not open camera.")
    exit()

# Get the actual resolution of the camera
frame_width = int(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
frame_height = int(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))

# Create the VideoWriter object with the actual resolution
output = cv2.VideoWriter('basics_opencv_video.avi', cv2.VideoWriter_fourcc(*'XVID'), 20, (frame_width, frame_height))

while video_capture.isOpened():
    ret, frame = video_capture.read()

    # Check if the frame was read correctly
    if ret:
        text = "Width: " + str(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH)) + " Height: " + str(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
        current_time = datetime.datetime.now()
        frame = cv2.putText(frame, (text+' '+str(current_time)), (10, 50), cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 255), 2, cv2.LINE_AA)

        # Write the frame to the output video
        output.write(frame)

        # Display the frame
        cv2.imshow('Video', frame)

        # Break the loop if 'q' is pressed
        if cv2.waitKey(1) == ord('q'):
            break
    else:
        print("Error: Could not read frame.")
        break

# Release the resources
video_capture.release()
output.release()
cv2.destroyAllWindows()







# import cv2
# video_capture = cv2.VideoCapture(0)
# output_file = 'basics_opencv_video.avi'
# output = cv2.VideoWriter(output_file, cv2.VideoWriter_fourcc(*'XVID'), 20, (640, 480))
#
# while video_capture.isOpened():
#     ret, frame = video_capture.read()
#     output.write(frame)
#     print(video_capture.get(cv2.CAP_PROP_FRAME_WIDTH))
#     print(video_capture.get(cv2.CAP_PROP_FRAME_HEIGHT))
#     if ret == True:
#         cv2.imshow('Video', frame)
#         if cv2.waitKey(1) == ord('q'):
#             break
#         # gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
#         cv2.imshow('Video', frame)
#         # cv2.imshow('Video', gray)
#
#     # if cv2.waitKey(1) == ord('q'):
#     #     break
# video_capture.release()
# output.release()
# cv2.destroyAllWindows()
#     # ret is True if the frame is read correctly, otherwise it is False
#     # frame is the frame that is read
#     # frame is a numpy array
#     # print(ret)
#     # print(frame)
#     # print(type(frame))
#     # print(frame.shape)
#     # print(frame.ndim)
#     # print(frame.size)
#     # print(frame.dtype)
#     # print(frame.item(0, 0, 0))
#     # print(frame.item(0, 0, 1))
#     # print(frame.item(0, 0, 2))
#     # print(frame.item(0, 0, 3))
#     # print(frame.item(0, 0, 4))
#     # print(frame.item(0, 0, 5))
#     # print(frame.item(0, 0, 6))
#     # print(frame.item(0, 0, 7))
#     # print(frame.item(0, 0, 8))
#     # print(frame.item(0, 0, 9))
#     # print(frame.item(0, 0, 10))
#     # print(frame.item(0, 0, 11))
#     # print(frame.item(0, 0, 12))
#     # print(frame.item(0, 0, 13))
#     # print(frame.item(0, 0, 14))
#     # print(frame.item(0, 0, 15))
#     # print(frame.item(0, 0, 16))
#     # print(frame.item(0, 0, 17))
#     # print(frame.item(0, 0, 18))
#     # print(frame.item(0, 0, 19))
#     # print(frame.item(0, 0, 20))
#     # print(frame.item(0, 0, 21))
#     # print(frame.item(0, 0, 22))
#     # print(frame.item(0, 0, 23))
#     # print(frame.item(0, 0, 24))
#     # print(frame.item(0, 0, 25))
#     # print(frame.item(0, 0, 26))
#     # print(frame.item(0, 0, 27))
#     # print(frame.item(0, 0, 28))
#     # print(frame.item(0,