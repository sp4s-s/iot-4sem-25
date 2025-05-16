import face_recognition
import cv2
import numpy as np
import pandas as pd
import os
from datetime import datetime

KNOWN_FACES_DIR = 'known_faces'
ATTENDANCE_DIR = 'attendance'

os.makedirs(ATTENDANCE_DIR, exist_ok=True)

known_encodings = []
known_names = []

for filename in os.listdir(KNOWN_FACES_DIR):
    if filename.endswith(('.jpg', '.jpeg', '.png')):
        image_path = os.path.join(KNOWN_FACES_DIR, filename)
        image = face_recognition.load_image_file(image_path)
        encodings = face_recognition.face_encodings(image)
        if encodings:
            known_encodings.append(encodings[0])
            name = os.path.splitext(filename)[0]
            known_names.append(name)
        else:
            print(f"Warning: No faces found in {filename}")

video_capture = cv2.VideoCapture(0)

print("Press 'q' to quit.")
attendance_marked = set()

while True:
    ret, frame = video_capture.read()
    if not ret:
        break

    # Resize frame for faster processing
    small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
    # Convert BGR to RGB
    rgb_small_frame = small_frame[:, :, ::-1]

    # Find all face locations and encodings in the current frame
    face_locations = face_recognition.face_locations(rgb_small_frame)
    face_encodings = face_recognition.face_encodings(rgb_small_frame, face_locations)

    for face_encoding in face_encodings:
        # Compare face with known faces
        matches = face_recognition.compare_faces(known_encodings, face_encoding)
        name = "Unknown"

        # Use the known face with the smallest distance if a match was found
        face_distances = face_recognition.face_distance(known_encodings, face_encoding)
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_names[best_match_index]

            if name not in attendance_marked:
                attendance_marked.add(name)
                now = datetime.now()
                date_str = now.strftime("%Y-%m-%d")
                time_str = now.strftime("%H:%M:%S")
                attendance_file = os.path.join(ATTENDANCE_DIR, f"attendance_{date_str}.csv")

                # Write to CSV
                if os.path.exists(attendance_file):
                    df = pd.read_csv(attendance_file)
                else:
                    df = pd.DataFrame(columns=['Name', 'Time'])

                df = df.append({'Name': name, 'Time': time_str}, ignore_index=True)
                df.to_csv(attendance_file, index=False)
                print(f"Marked attendance for {name} at {time_str}")


    cv2.imshow('Attendance Window', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()
