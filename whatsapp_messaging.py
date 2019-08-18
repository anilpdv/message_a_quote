from twilio.rest import Client
from apscheduler.schedulers.blocking import BlockingScheduler
import requests

# creating scheduler instance
scheduler = BlockingScheduler()


@scheduler.scheduled_job('interval', minutes=30)
def msg_mom_and_dad(event=None, context=None):

    # get your sid and auth token from twilio
    twilio_sid = 'ACc1e3421e932cf3d9b618c6bf084ca41e'
    auth_token = '089177c78b14b336a8ab82a1b7bccacc'

    whatsapp_client = Client(twilio_sid, auth_token)

    # keep adding contacts to this dict to send
    # them the message
    contact_directory = {'daddy': '+918179608406'}
    quote = requests.get('http://quotesapi.ml/random')
    data = quote.json()

    msg = data['quote'] + '  -  ' + data['author'].replace(',', '')

    for key, value in contact_directory.items():
        msg_loved_ones = whatsapp_client.messages.create(
            body=msg,
            from_='whatsapp:+14155238886',
            to='whatsapp:' + value,
            media_url='https://picsum.photos/300/300')

        print(msg_loved_ones.sid)


scheduler.start()
