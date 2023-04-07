import random
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor
from reportlab.lib.units import inch
from reportlab.pdfgen import canvas
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.application import MIMEApplication
import uploadGoogleCloud


def send(name,age,emailId,contact,symptoms,predicted_value):
    num=random.randint(100000000,999999999)
    # create PDF canvas
    c = canvas.Canvas("medical_report.pdf", pagesize=letter)
    # add hospital image on the top left corner
    c.drawImage("static\images\logoo.png", 20, 650, width=1.5*inch, height=1.5*inch)
    # add report details
    c.drawString(1*inch, 600, f"Report ID: {num}")
    c.drawString(1*inch, 575, f"Name: {name}")
    c.drawString(1*inch, 525, f"Age: {age}")
    c.drawString(1*inch, 500, f"Phone No.: {contact}")
    c.drawString(1*inch, 475, f"Email: {emailId}")
    c.drawString(1*inch, 425, f"Symptoms: {symptoms}")
    # add medical report result
    c.drawString(1*inch, 400, f"Medical Report Result: {predicted_value}")
    # Set the font color to red
    c.setFillColor(HexColor("#FF0000"))
    # Set the font to bold and italic
    c.setFont("Helvetica-BoldOblique", 30)
    # add hospital name
    c.drawString(2*inch, 700, "ALZEHIMERS'S REPORT")
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
        attach = MIMEApplication(f.read(),_subtype = "pdf")
        attach.add_header('Content-Disposition','attachment',filename="medical_report.pdf")
        msg.attach(attach)

    # SMTP server login
    username = "1NH20CS124@gmail.com"
    password = "xphclqhvzzihmrio"
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login(username, password)

    # send email
    text = msg.as_string()
    server.sendmail(fromaddr, toaddr, text)

    # close SMTP server
    server.quit()
    uploadGoogleCloud.uploadtocloud()
