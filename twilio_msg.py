from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv()

TWILIO_SID = os.getenv("TWILIO_SID")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN")
TWILIO_WHATSAPP_NUMBER = os.getenv("TWILIO_WHATSAPP_NUMBER")
YOUR_WHATSAPP = os.getenv("YOUR_WHATSAPP")

client = Client(TWILIO_SID, TWILIO_AUTH_TOKEN)

def send_whatsapp_message(message):
    client.messages.create(
        body=message,
        from_=TWILIO_WHATSAPP_NUMBER,
        to=YOUR_WHATSAPP
    )
    print("✅ WhatsApp message sent!")

__all__ = ["send_whatsapp_message"]