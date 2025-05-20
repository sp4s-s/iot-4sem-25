import torch
from torchvision import transforms
from facenet_pytorch import InceptionResnetV1, MTCNN
import cv2
import numpy as np
from PIL import Image
from scipy.spatial.distance import cosine


device = 'cuda' if torch.cuda.is_available() else 'cpu'


mtcnn = MTCNN(image_size=160, margin=0, keep_all=False, device=device)


model = InceptionResnetV1(pretrained='vggface2').eval().to(device)

def extract_face_embedding(image_path):
    img = Image.open(image_path).convert('RGB')
    face = mtcnn(img)
    if face is None:
        raise ValueError("No face detected in image.")
    face_embedding = model(face.unsqueeze(0).to(device))
    return face_embedding.detach().cpu().numpy()[0]

def compare_faces(embedding1, embedding2, threshold=0.6):
    distance = cosine(embedding1, embedding2)
    match = distance < threshold
    return match, distance


reference_embedding = extract_face_embedding("../data/s1.jpg") 


input_embedding = extract_face_embedding("../data/s2.jpg") 

match, score = compare_faces(reference_embedding, input_embedding)

print(f"Match: {match}, Similarity Score: {1 - score:.4f}")

