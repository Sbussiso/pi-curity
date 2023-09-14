from twilio.rest import Client

def send_sms_via_twilio(body, to_number):
    # Your Twilio account SID and Auth Token
    ACCOUNT_SID = 'ACf6b99f2fa295d00137eb6153bbadffa3'
    AUTH_TOKEN = 'c490b87d779a5d0a2dfac8e47a9d92b0'

    # Your Twilio phone number (purchased on Twilio dashboard)
    TWILIO_PHONE_NUMBER = '+18332060227'

    client = Client(ACCOUNT_SID, AUTH_TOKEN)

    message = client.messages.create(
        body=body,
        from_=TWILIO_PHONE_NUMBER,
        to=to_number
    )

    return message.sid  # Returns the message ID (SID)
