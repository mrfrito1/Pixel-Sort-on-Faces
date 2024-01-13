import cv2
import os
import numpy as np
from tqdm import tqdm

# Path to the 'frames' folder
frames_folder = '/Users/g.s.e/Programacion/VideoDxm/frames'

# Path to the 'haarcascade_frontalface_default.xml' file
classifier_path = '/Users/g.s.e/Programacion/VideoDxm/haarcascade_frontalface_default.xml'

# Create a new folder named 'face_masks' if it doesn't exist
if not os.path.exists('face_masks'):
    os.makedirs('face_masks')

# Load the 'haarcascade_frontalface_default.xml' classifier
face_cascade = cv2.CascadeClassifier(classifier_path)

# Iterate through each file in the 'frames' folder with a progress bar
for file in tqdm(os.listdir(frames_folder)):
    # Load the image
    image = cv2.imread(os.path.join(frames_folder, file))
    
    # Check if the image was loaded successfully
    if image is None:
        print(f"Error: Unable to load image {file}")
        continue
    
    # Convert the image to grayscale
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    
    # Detect faces in the image using the 'haarcascade_frontalface_default.xml' classifier
    faces = face_cascade.detectMultiScale(gray, 1.3, 5)
    
    # Create a new image with a black background of the same size as the original image
    mask = np.zeros_like(image)
    
    # Iterate through each detected face
    for (x, y, w, h) in faces:
        # Draw a white rectangle over the detected face
        cv2.rectangle(mask, (x, y), (x+w, y+h), (255, 255, 255), -1)
    
    # Save the resulting mask image in the 'face_masks' folder
    cv2.imwrite(os.path.join('/Users/g.s.e/Programacion/VideoDxm/face_masks', file), mask)