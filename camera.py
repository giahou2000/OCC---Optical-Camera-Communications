import cv2

# Connect to the camera
cap = cv2.VideoCapture(0)

# Loop through the frames
while True:
    # Capture a frame
    ret, frame = cap.read()

    # grayframe = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # (thresh, bnwFrame) = cv2.threshold(grayframe, 127, 255, cv2.THRESH_BINARY)

    # Display the frame
    cv2.imshow('frame', frame)

    # Process the frame here...

    # Check for quit key
    if cv2.waitKey(1) == ord('q'):
        break

# Release the camera and close the window
cap.release()
cv2.destroyAllWindows()