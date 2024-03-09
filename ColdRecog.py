import os
import streamlit as st
from PIL import Image
from deepface import DeepFace
import firebase_admin
from firebase_admin import credentials, storage
from io import BytesIO

# Load Firebase credentials and initialize the app with storage configuration
if not firebase_admin._apps:
    cred = credentials.Certificate('auth.json')
    firebase_admin.initialize_app(cred, {'storageBucket': 'coldrecog.appspot.com'})

    # Access the default Cloud Storage bucket
    bucket = storage.bucket()

    # Define the folder path in the bucket
    folder_path = 'aadhar'  # Replace with the correct folder path
else:
    # Access the default Cloud Storage bucket
    bucket = storage.bucket()
    # Define the folder path in the bucket
    folder_path = 'aadhar'  # Replace with the correct folder path

# List all the blobs (files) in the specified folder path
blobs = bucket.list_blobs(prefix=folder_path)

# Temporary file path for storing the downloaded reference image
reference_img_path = "temp.jpg"
final_img_path = "result.jpg"

# Function to process uploaded image and perform matching
def process_image(uploaded_image):
    try:
        # Convert the uploaded image file to bytes
        image_bytes = uploaded_image.read()

        # Convert bytes data to PIL Image
        img = Image.open(BytesIO(image_bytes))
        img.save(test_img_path)
        minMatch = 100
        threshold = 60 

        # Delete the old result.jpg file if it exists
        if os.path.exists(final_img_path):
            os.remove(final_img_path)

        # Loop through each blob in the specified folder
        for blob in blobs:
            try:
                # Get the file path of the current blob
                file_path = blob.name

                # Skip if the file path corresponds to the folder itself
                if file_path == "aadhar/":
                    continue

                # Download the image data from the current blob
                blob = bucket.blob(file_path)
                image_data = blob.download_as_bytes()
                # Save the downloaded image locally
                local_file_path = f'./{reference_img_path}'
                with open(local_file_path, 'wb') as local_file:
                    local_file.write(image_data)

                # Use DeepFace library to verify similarity between reference and test images
                result = DeepFace.verify(reference_img_path, test_img_path)
                match_rate = round(result["distance"] * 100, 2)
                if match_rate < minMatch and match_rate < threshold:
                    minMatch = match_rate
                    # store the potential result
                    local_file_path = f'./{final_img_path}'
                    with open(local_file_path, 'wb') as local_file:
                        local_file.write(image_data)
                # Remove the temporary reference image file
                if minMatch == match_rate:
                    os.remove(reference_img_path)

            except Exception as e:
                continue

        # Display the uploaded image and matched image side by side
        col1, col2 = st.columns(2)
        with col1:
            st.image(img, caption="Uploaded Image", width=250)
        with col2:
            if os.path.exists(final_img_path):
                matched_img = Image.open(final_img_path)
                st.image(matched_img, caption="Matched Image", width=250)
            else:
                st.error("No match found.")

    except Exception as e:
        st.error(f"Error processing the uploaded image: {e}")

# CSS styling
st.markdown(f"""
    <style>
        /* Add your CSS styling here */
            
        body {{
            background-color: #ffffff; /* Set background color to white */
            font-family: 'Arial', sans-serif;
        }}
        h1 {{
            color: #ffffff;
            font-size: 2.5rem;
            margin-bottom: 20px;
        }}
    </style>
""", unsafe_allow_html=True)

# Set page title and favicon
st.markdown('<link rel="shortcut icon" href="favicon.ico">', unsafe_allow_html=True)
st.markdown("<title>FaceRecog</title>", unsafe_allow_html=True)

# Streamlit app content
st.title("FaceRecog")

# Allow user to upload an image
uploaded_image = st.file_uploader("Upload a test image", type=["jpg", "jpeg", "png"])

# Path to the test image
test_img_path = "./uploaded_test_image.png"  # Temporarily store the uploaded image

# Process the uploaded image if available
if uploaded_image is not None:
    process_image(uploaded_image)