import sendgrid
import os
from sendgrid.helpers.mail import *

# def substitute(string, dict):
#     for count, val in enumerate(dict):
#         string = string.replace(list(dict.keys())[count], str(list(dict.values())[count]))
#     return string

def main():
    message = Mail(
    from_email=From("barnstableairlines@gmail.com", "Barnstable Airlines"),
    to_emails='dylanmatthewheadley@gmail.com',
    )

    message.dynamic_template_data = {
        'confirmation_code': 'confirmation_code',
        'from': 'departure_location',
        'to': 'arrival_location',
        'date': 'boarding_date',
        'time': 'boarding_time',
        'plane': 'aircraft_type',
        'capacity': 'flight_capacity',
        'name': 'customer_name',
        'cost': 'flight_cost',
        'taxes': 'flight_taxes',
        'total_cost': 'total_cost'
    }

    message.template_id = 'd-70ed94c0f90341079e91891802b55d6a'

    try:
        sendgrid_client = sendgrid.SendGridAPIClient(api_key=os.environ.get('SENDGRID_API_KEY'))
        sendgrid_client.send(message)
    except Exception as e:
        print(e.body)

if __name__ == '__main__':
    main()