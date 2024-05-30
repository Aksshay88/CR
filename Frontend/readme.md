<div align=center>
<img src="https://www.intel.com/content/dam/develop/public/us/en/images/logos/logo-oneapi-rwd.png" width=300>
<img src="../images/Logomain.png" alt="png" width="190">
<h1>INTEL ONE API HACKATHON 2024</h1> 
<img src="https://img.shields.io/badge/intel-%23121011?style=for-the-badge&color=blue">
<img src="https://img.shields.io/badge/daksh-%23121011?style=for-the-badge&logoColor=%23ffffff&color=%23000000">
<img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&color=black">
</div>
<br>

# Tech Stack
<img src="https://img.shields.io/badge/GitHub-100000?style=for-the-badge&logo=github&logoColor=white"><img src="https://img.shields.io/badge/website-000000?style=for-the-badge&logo=About.me&logoColor=white"><img src="https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white">

## Overview

This project is a face recognition application built using Streamlit for the frontend and Firebase for backend storage. It allows users to perform face recognition on uploaded images and associates them with person identities stored in a Firebase database.
## How does it work

1. Upload a picture of the person you want to compare
2. Click compare and it will compare the face found in picture.
   - Check the size of picture uploaded. If is above certain threshold, then it will be compress </br>
     <img src="../images/flowchartpng.png" alt="Flowchart" style="width: 70%; height: 70%;">

</br>
# Face Recognition App with Streamlit and Firebase


# Intel® oneAPI is used to optimize the models to provide accurate and efficient prediction,


### Key Features
- **Image Comparison:** Utilizing advanced image processing and deep learning techniques to compare uploaded images with reference data.
- **Aadhar Verification:** Verifying identity against Aadhar images to ensure accurate identification.
- **Streamlit Interface:** User-friendly Streamlit interface for seamless interaction and quick results.
# How to Use
## Installation

Clone the repository:

```bash
git clone https://github.com/Ren-Gen22/coldRecog.git
```

```bash
cd coldRecog
```

# FOR Windows

 Create a virtual environment

```cmd
python -m venv venv
```

Activate the virtual environment

```cmd
venv\Scripts\activate
```

Install dependencies (replace requirements.txt with your actual requirements file)

```cmd
pip install -r requirements.txt
```

Deactivate the virtual environment when done

```cmd
deactivate
```

# For Linux:

```bash

python3 -m venv venv
```

Activate the virtual environment

```bash
source venv/bin/activate
```

```bash
pip install -r requirements.txt
```

Deactivate the virtual environment when done

```bash
deactivate
```
