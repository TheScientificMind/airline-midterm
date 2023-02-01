import sendgrid
import os
from sendgrid.helpers.mail import *

"""
def substitute(string, dict):
    for count, val in enumerate(dict):
        string = string.replace(list(dict.keys())[count], str(list(dict.values())[count]))
   return string
"""

# sends an email to a customer with the given information
def sendEmail(customer_email, code, origin, destination, date, time, aircraft, capacity, name, cost):
    # user and system emails
    message = Mail(
    from_email=From("barnstableairlines@gmail.com", "Barnstable Airlines"),
    to_emails=customer_email,
    )

    # replace values with data
    message.dynamic_template_data = {
        'confirmation_code': code,
        'from': origin,
        'to': destination,
        'date': date,
        'time': time,
        'plane': aircraft,
        'capacity': capacity,
        'name': name,
        'cost': "$" + cost,
        'taxes': "$" + str(int(cost) * .065),
        'total_cost': "$" + str(int(cost) * 1.065),
    }

    # dynamic html email template id
    message.template_id = 'd-70ed94c0f90341079e91891802b55d6a'

    # tries to send email
    try:
        sendgrid_client = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        sendgrid_client.send(message)
    except Exception as e:
        print(e.body)