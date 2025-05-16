import face_recognition

image1 = face_recognition.load_image_file("s1.jpeg")
image2 = face_recognition.load_image_file("s2.jpeg")

encodings1 = face_recognition.face_encodings(image1)
encodings2 = face_recognition.face_encodings(image2)

if encodings1 and encodings2:
    result = face_recognition.compare_faces([encodings1[0]], encodings2[0])
    print("Same person" if result[0] else "Different people")
else:
    print("Face not detected in one or both images.")




