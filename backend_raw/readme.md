<div align=center>
<img src="https://www.intel.com/content/dam/develop/public/us/en/images/logos/logo-oneapi-rwd.png" width=300>
<img src="../images/Logomain.png" alt="png" width="190">
<h1>INTEL ONE API HACKATHON 2024</h1> 
<img src="https://img.shields.io/badge/intel-%23121011?style=for-the-badge&color=blue">
<img src="https://img.shields.io/badge/daksh-%23121011?style=for-the-badge&logoColor=%23ffffff&color=%23000000">
<img src="https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&color=black">
</div>
<br>

# Backend
<i><b>Tech Stack:</b></i>

![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white)
![Firebase](https://img.shields.io/badge/firebase-a08021?style=for-the-badge&logo=firebase&logoColor=ffcd34)


The backend part of the application is to classify the backend in a modular manner, which are,

<b><i>FireBase:</i></b>
    <br />
   Firebase Storage provides a robust, scalable, and secure solution for storing and retrieving images in your web or mobile applications. This integration guide outlines the key steps to implement image management with Firebase Storage, ensuring a smooth and efficient experience for your users.
   <b>Prerequisites:</b>

A Firebase project (https://firebase.google.com/docs/projects/api/workflow_set-up-and-manage-project)</br>
Firebase Storage enabled for your project (https://firebase.google.com/docs/storage/web/start)
A basic understanding of your chosen development environment (Android, iOS, web, etc.)</br>
Steps:

<b>Set up Firebase Storage:</b></br>

Follow the official Firebase documentation (https://firebase.google.com/docs/storage/web/start) to enable Firebase Storage in your project. This typically involves adding the Firebase Android SDK or Firebase JavaScript SDK to your project.

<b>Upload Images:</b></br>

Use the appropriate Firebase Storage SDK methods to upload images from your client-side application. Here's a general outline (consult the specific documentation for your platform for detailed code examples):
Create a reference to the storage location in your Firebase project using getReference().
Select the image file from the user's device or application using a file picker.
Upload the image file to the storage reference using putFile() or equivalent methods.
Remember to handle potential errors during the upload process and provide informative feedback to the user.
Retrieve Images:</br>

Once uploaded, images can be retrieved using their download URLs obtained during the upload process. Here's a general structure:
Create a reference to the image using getReference().
Get the download URL using getDownloadUrl().
Use the download URL in your application's image view component or for further processing as needed.

<b>Security Considerations:</b></br>

Firebase Storage offers robust security rules to control access to your stored images. Implement appropriate rules to restrict unauthorized access based on user authentication or other criteria. Refer to the Firebase documentation for security rule configuration (https://firebase.google.com/docs/storage/security).
Consider additional measures like image compression or resizing to optimize storage usage and bandwidth consumption.
    <br />
    <br />
    <b>Actions:</b>
    <br />
    <ul>
        <li>Checks the image that has been provided by the user .</li>
        <li>Identifies the identity of the person.</li>
        <li>Recalculate the person's face for better results.</li>
    </ul>
