from picamera2 import Picamera2
import cv2

# Initialize Picamera2
picam2 = Picamera2()
picam2.preview_configuration.main.size = (640, 480)
picam2.preview_configuration.main.format = "RGB888"
picam2.configure("preview")
picam2.start()

# Display loop
print("Camera feed started. Press 'q' to quit.")
while True:
    frame = picam2.capture_array()
    cv2.imshow("Live Camera Feed", frame)

    # Quit on 'q' key
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Cleanup
cv2.destroyAllWindows()
picam2.stop()

