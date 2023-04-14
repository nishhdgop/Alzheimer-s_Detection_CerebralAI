# CerebralAI : Alzheimer's Disease Detection

## Introduction :

Alzheimer's disease is a neurodegenerative disease that affects various essential functions of the brain like memory and comprehension, and affects a large population of the world. This disorder is a primary cause of dementia and is the fifth-leading cause of deaths among older people. According to reports, the number of people suffering from dementia is set to cross the 11 million mark in India. 

Also, since India is unfortunately the diabetic capital of the world, more than 11 million diabetic patients in our country are at the severe risk of contracting this disorder. Since Alzheimer's disease doesn't have any cure, it is imperative that the detection of the disease be done at the earliest. This will increase the chances of the administration of a timely treatment, which will be more effective, and help slow down the progress of the disease.

## The Problem :

The detection of this disease can be done through analyzing of MRI or CT scans by radiologists and neurologists, or through comprehensive neurological exams by an experienced neuropsychologist, that are designed to make cognitive and functional assessments of the brain. 

However, majority of Indians, especially those residing in rural areas have no access to centres of neurological excellence in the country. This, coupled with the lack of neuroscience specialists and an increase in our aging population, poses a major problem in the country.

## Our Solution :

Our interactive web-application : CerebralAI, seeks to solve this issue. CerebralAI provides a lucid, easy-to-use platform for the detection of this deadly disorder. With modern technology and a deep learning model, we provide patients with a quick and accurate diagnosis of their current stage of Alzheimer's disease by analyzing their brain scans. 

Our aim is to reduce the mortality rate among the elderly due to Alzheimer's disease, by providing an efficient and speedy diagnosis of the disorder, and help better the quality of life of every patient suffering from dementia.

## Aspects of CerebralAI :

Our web-application has an interface that is user-friendly and can be used by anyone - be it patients, their family members or medical professionals. The patient can upload their MRI scan into our model through the interface along with their details like name, age, gender, email, symptoms etc. On the basis of their uploaded MRI scan, our trained deep learning model conducts an analysis and detects the stage of Alzheimer's disease that the patient has with 93% accuracy. We have four stages of classification : Non Demented, Very Mild Demented, Mild Demented and Moderate Demented. A report is generated and the same is sent to the email ID provided by the patient. 

It is also uploaded in our Google Cloud, which can be used by the patient for future reference. For any other queries and FAQs that might occur to the user, we also have a chatbot that caters to their needs.

## Our Features :

   - Detection of 4 stages of Alzheimer's disease.
   - Interactive UI-based web-app
   - A chatbot on our web-app for service assistance and FAQs.
   - Generated DR report is sent to patient’s email.
   - This report is also backed up on our Google Cloud Platform for documentation and future reference pueposes.

## Technologies used for development : 

### Frontend :

- **HTML and CSS**:- Used to create a visually appealing webpage and add styling, layout and control the look and feel of the website. 

- **Flask**:- It is a lightweight, open source web application framework for Python that we have used to deploy the deep learning model to the website.

### Backend :

- **Google Cloud**:- We have made use of the Google Cloud's flexible data storage system in order to store the generated diagnosis reports as it offers safe and secure storage systems with easy file retrieval mechanism.

- **AMD instances**:- Our project CerebralAI has been deployed on the AMD Virtual Machine instance combining the powerful capabilities of AMD virtual machine running on the Google Cloud Platform.
 
- **Google's TensorFlow**:- We have used tensorflow API to train our model to predict the current stage of Alzheimer's disease based on the brain scan image uploaded by the user.

- **KerasAPI**:- Keras is a high level neural network library. We have used it to train our deep learning model using the VGG19 Algorithm.

- **VGG19**:- VGG19 is a deep convolutional neural network model used for image classification tasks. It consists of 19 layers, including 16 convolutional layers, 3 fully connected layers, and a final softmax classifier layer. Our project uses over 6000 brain scan images to train the model.

## Project Implementation :

1. AMD instances and Google Cloud:- The project is deployed on the amd virtual machine instance running on the google cloud platform and is run through the command line.
 
   <img width="800" src="https://user-images.githubusercontent.com/116015331/231960522-98a8e786-608b-4b11-8133-60ca3c2acd80.png">

2. Homepage of CerebralAI- This page displays the CerebralAI web app user interface

   <img width="800" src="https://user-images.githubusercontent.com/116015331/231774032-e74d2d07-41e5-4237-9bba-6b062100ec19.png">

3. User Interface 2- This page displays the About Us content of the web app.

   <img width="800" src="https://user-images.githubusercontent.com/116015331/231774601-5fbfaa04-9f47-4ccd-9b69-ee7d229fbd28.png">

4. Chatbot- It shows the chatbot implementation in the web app.

   <img width="800" src="https://user-images.githubusercontent.com/116015331/231775150-33588359-6d45-4069-a0fd-fca2899bc1ba.png">

5. Alzheimer's disease prediction- The brain scan image is uploaded to predict the current stage of Alzheimer's disease.

   <img width="800" src="https://user-images.githubusercontent.com/116015331/231774892-869dd9e9-38ad-4561-aa63-55aba7bfe5f4.png">

6. Email Generation-  The email is generateed once the prediction happens from the image uploaded by the user. The email consists of an attachment of the medical report generated.

   <img width="800" src="https://user-images.githubusercontent.com/116015331/231775415-7aa85284-f43c-47f5-b2de-0469f87d56b5.png">

7. Google Cloud Storage- The generated report after prediction is also stored in the Google Cloud Platform for future refernces and documentation purposes. 

   <img width="800" src="https://user-images.githubusercontent.com/116015331/231775845-f5f4fe05-a262-46a1-b17e-cfb2cc0a6322.png">
   
## Our unique value proposition :
This is **CerebralAI**.
We provide an interactive user-friendly interface for patients to  use, so that anyone can have access to a quick and free diagnosis of Alzheimer's disease. By **SOLVING FOR INDIA** our vision is to help every Indian at the risk of or suffering from dementia and enable them to lead quality life.

