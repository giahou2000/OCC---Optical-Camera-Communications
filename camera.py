import cv2

# Connect to the camera
cap = cv2.VideoCapture(1)

# Loop through the frames
while True:
    # Capture a frame
    ret, frame = cap.read()

    # # binary transformation
    # grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # (thresh, bnwFrame) = cv2.threshold(grayframe, 127, 255, cv2.THRESH_BINARY)
    # # Display the frame
    # cv2.imshow('frame', bnwFrame)

    # Display the frame
    y_min = 60
    y_max = 360
    x_min = 360
    x_max = 665
    useful_frame = frame[y_min:y_max, x_min:x_max]
    cv2.imshow('frame', useful_frame)
    # print(frame.shape)

    # Process the frame here...

    # Check for quit key
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()