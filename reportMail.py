import random
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.lib.colors import black
from reportlab.pdfgen import canvas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import uploadGoogleCloud
import datetime


def send(name, age, emailId, contact, symptoms, predicted_value):
    num = random.randint(100000000, 999999999)
    current_time = datetime.datetime.now()
    # create PDF canvas
    c = canvas.Canvas("medical_report.pdf", pagesize=letter)
    c.setStrokeColor(black)
    c.rect(0.5*inch, 0.5*inch, letter[0]-1*inch, letter[1]-1*inch)

    # add hospital image on the top left corner
    c.drawImage("static\images\gfglogo.png", 60, 650,
                width=2*inch, height=1*inch)
    # add report details
    c.drawString(4*inch, 500, f"Date/Time: {current_time}")
    c.drawString(1*inch, 500, f"Report ID: {num}")
    c.drawString(1*inch, 475, f"Name: {name}")
    c.drawString(1*inch, 450, f"Age: {age}")
    c.drawString(1*inch, 425, f"Phone No.: {contact}")
    c.drawString(1*inch, 400, f"Email: {emailId}")
    c.drawString(1*inch, 375, f"Symptoms: {symptoms}")
    # add medical report result
    c.drawString(
        1*inch, 350, f"Medical Report Result: Patient is identified to be {predicted_value}")
    if predicted_value == 'MildDemented':
        text = """Further advice to be followed:

        1. Patient is in an early stage of Alzheimer's.
        2. However, with proper treatment and care, the advent of the disease can be slowed.
        3. We advise you to visit your primary care provider at the earliest to begin treatment.
        4. Alzheimer's is a disease that gets worse as time progresses. We strongly recommend 
           that the patient and the family take serious steps to combat it."""

    elif predicted_value == 'VeryMildDemented':
        text = """Further advice to be followed :

        1. Patient is in the very early stage of Alzheimer's.
        2. However, with proper treatment and care, the advent of the disease can be slowed.
        3. We recommend that you visit your primary care provider at the earliest to begin 
           treatment."""
    elif predicted_value == 'ModerateDemented':
        text = """Further advice to be followed :

        1. Patient is in a serious stage of Alzheimer's.
        2. Immediate treatment should begin at the earliest.
        3. We advise you to visit your primary care provider as soon as possible.
        4. Alzheimer's is a disease that gets worse as time progresses. We strongly 
           recommend that the patient and the family take serious steps to combat it."""
    elif predicted_value == 'NonDemented':
        text = """Further advice to be followed :

        1. Patient is not suffering from Alzheimer's yet.
        2. However, we recommend making healthy lifestyle choices to lower your risk 
           of Alzheimer's:
        - Prevent and manage high blood pressure levels
        - Manage blood sugar levels
        - Maintain a healthy weight
        - Be physically active
        - Get enough sleep"""

    # Create a text object
    textobject = c.beginText()

    # Set the position for the text object
    textobject.setTextOrigin(1*inch, 325)

    # Set the font and font size
    textobject.setFont("Helvetica", 12)

    # Add the text with multiple lines using the textLines() method
    textobject.textLines(text)

    # Draw the text on the canvas
    c.drawText(textobject)

    # Set the font color to green
    # c.setFillColor(HexColor("#006400"))
    # # Set the font to bold and italic
    # c.setFont("Helvetica-Bold", 40)
    # # add hospital name
    # c.drawString(3*inch, 650, "CEREBRAL AI")
    c.setFillColor(HexColor("#006400"))
    c.setFont("Helvetica", 10)
    c.drawString(
        1*inch, 100, "This report will be sent to the email ID mentioned by the patient. A copy will be also be available in")
    c.drawString(
        1*inch, 80, "our Google Cloud, for any future references needed by the patient.")
    # c.setFont("Helvetica", 15)
    # c.drawString(3.1*inch, 630, "Delivering your hopes .......")
    c.setFont("Helvetica-BoldOblique", 35)
    c.drawString(2.1*inch, 580, "Alzheimer's report")
    # save PDF file
    c.save()

    # send email with PDF attachment
    fromaddr = "1NH20CS124@gmail.com"
    toaddr = emailId

    msg = MIMEMultipart()
    msg['From'] = fromaddr
    msg['To'] = toaddr
    msg['Subject'] = "Alzheimer Report"

    body = "Please find attached the medical report."

    msg.attach(MIMEText(body, 'plain'))

    with open("medical_report.pdf", 'rb') as f:
        attach = MIMEApplication(f.read(), _subtype="pdf")
        attach.add_header('Content-Disposition', 'attachment',
                          filename="medical_report.pdf")
        msg.attach(attach)

        # SMTP server login
        username = "1NH20CS124@gmail.com"
        password = "****************"#cannot be public
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls()
        server.login(username, password)

        # send email
        text = msg.as_string()
        server.sendmail(fromaddr, toaddr, text)

        # close SMTP server
        server.quit()
        uploadGoogleCloud.uploadtocloud()
