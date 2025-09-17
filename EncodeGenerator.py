import cv2
import face_recognition
import pickle
import os

# Path where student images are stored
folderPath = "Images"  # Ensure this folder contains your 216x216 images
studentIds = [os.path.splitext(img)[0] for img in os.listdir(folderPath)]  # Extract student IDs

# Load images and process them
imgList = []
for imgName in studentIds:
    imgPath = os.path.join(folderPath, imgName + ".png")  # Ensure correct format
    img = cv2.imread(imgPath)

    if img is None:
        print(f"Error: Unable to load image {imgPath}")
        continue  # Skip invalid images

    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Convert to RGB (required for face_recognition)
    imgList.append(img)

# Function to generate encodings
def findEncodings(imagesList):
    encodeList = []
    for img in imagesList:
        encodings = face_recognition.face_encodings(img)
        if len(encodings) > 0:
            encodeList.append(encodings[0])  # Store only the first face encoding
        else:
            print("Warning: No face detected in one of the images!")
    return encodeList

# Generate encodings
print("Encoding process started...")
encodeListKnown = findEncodings(imgList)
print("Encoding complete!")

# Save the encodings and student IDs to a file
with open("EncodeFile.p", "wb") as file:
    pickle.dump((encodeListKnown, studentIds), file)

print("Encodings saved successfully!")
