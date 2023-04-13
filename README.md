# CerebralAI : Alzheimer's Disease Detection

## Introduction :

Alzheimer's disease is a neurodegenerative disease that affects various essential functions of the brain like memory and comprehension, and affects a large population of the world. This disorder is a primary cause of dementia and is the fifth-leading cause of deaths among older people. According to reports, the number of people suffering from dementia is set to cross the 11 million mark in India. 

Also, since India is unfortunately the diabetic capital of the world, more than 11 million diabetic patients in our country are at the severe risk of contracting this disorder. Since Alzheimer's disease doesn't have any cure, it is imperative that the detection of the disease be done at the earliest. This will increase the chances of the administration of a timely treatment, which will be more effective, and help slow down the progress of the disease.

## The Problem :

The detection of this disease can be done through analyzing of MRI or CT scans by radiologists and neurologists, or through comprehensive neurological exams by an experienced neuropsychologist, that are designed to make cognitive and functional assessments of the brain. 

However, majority of Indians, especially those residing in rural areas have no access to centres of neurological excellence in the country. This, coupled with the dearth of neuroscience specialists and an increase in our aging population, poses a major problem in the country.

## Our Solution :

Our interactive web-application : CerebralAI, seeks to solve this issue. CerebralAI provides a lucid, easy-to-use platform for the detection of this deadly disorder. With modern technology and a deep learning model, we provide patients with a quick and accurate diagnosis of their current stage of Alzheimer's disease by analyzing their brain scans. 

Our aim is to reduce the mortality rate among the elderly due to Alzheimer's disease, by providing an efficient and speedy diagnosis of the disorder, and help better the quality of life of every patient suffering from dementia.

## Features of CerebralAI :

Our web-application has an interface that is user-friendly and can be used by anyone - be it patients, their family members or medical professionals. The patient can upload their MRI scan into our model through the interface along with their details like name, age, gender, email, symptoms etc. On the basis of their uploaded MRI scan, our trained deep learning model conducts an analysis and detects the stage of Alzheimer's disease that the patient has with 93% accuracy. We have four stages of classification : Non Demented, Very Mild Demented, Mild Demented and Moderate Demented. A report is generated and the same is sent to the email ID provided by the patient. 

It is also uploaded in our Google Cloud, which can be used by the patient for future reference. For any other queries and FAQs that might occur to the user, we also have a chatbot that caters to their needs.

## Our Features :

   - Detection of 4 stages of Alzheimer's disease.
   - Interactive UI-based web-app
   - A chatbot on our web-app for service assistance and FAQs.
   - Generated DR report is sent to patient’s email.
   - This report is also backed up on our Google Cloud Platform for documentation and future reference pueposes.

## Technologies We Have Used : 

### Frontend :

- HTML
- CSS 
- Flask

### Backend :

- Google Cloud
- AMD instances
- Google's TensorFlow
- KerasAPI
- OpenCV
- Deep Learning
- VGG19
- CNN

## Output Screenshots :

Output 1: CerebralAI web app user interface

![Screenshot (289)](https://user-images.githubusercontent.com/116015331/231774032-e74d2d07-41e5-4237-9bba-6b062100ec19.png)

Output 2: User interfsce 2

![Screenshot (291)](https://user-images.githubusercontent.com/116015331/231774601-5fbfaa04-9f47-4ccd-9b69-ee7d229fbd28.png)

Output 3: ChatBot implementation in the web app.

![Screenshot (290)](https://user-images.githubusercontent.com/116015331/231775150-33588359-6d45-4069-a0fd-fca2899bc1ba.png)

Output 4: Alzheimer's disease prediction by uploading the MRI scan image

![Screenshot (293)](https://user-images.githubusercontent.com/116015331/231774892-869dd9e9-38ad-4561-aa63-55aba7bfe5f4.png)

Output 5:  The email is generateed once the prediction happens from the image uploaded by the user. The email consists of an attachment of the medical report generated.

![Screenshot (295)](https://user-images.githubusercontent.com/116015331/231775415-7aa85284-f43c-47f5-b2de-0469f87d56b5.png)

Output 6: The generated report after prediction is also stored in the Google Cloud Platform for future refernces and documentation purposes. 

![Screenshot (297)](https://user-images.githubusercontent.com/116015331/231775845-f5f4fe05-a262-46a1-b17e-cfb2cc0a6322.png)
