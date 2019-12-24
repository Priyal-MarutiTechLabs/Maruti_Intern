import os
import csv
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

data = []

with open('data2.csv', 'r') as csvfile:
    reader = csv.DictReader(csvfile)
    for row in reader:
        data1 = {}
        data1["first_name"]=row["First Name"]
        data1["email"]=row["Email"]
        data.append(data1)










for recipient in data:
    message = Mail(
    from_email='priyalpatel2024@gmail.com',
    to_emails=recipient['email'],

    )


    message.dynamic_template_data = {
    'first_name': recipient["first_name"],
    "meta": {
        "year": 2020
      }
    }
    message.template_id = "d-6cf8cd44336c4ab083b9cb9b9e332af3"
    try:
        sendgrid_client = SendGridAPIClient('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')

        response = sendgrid_client.send(message)
        print(response.status_code)
        print(response.body)
        print(response.headers)
    except Exception as e:
        print(e)
