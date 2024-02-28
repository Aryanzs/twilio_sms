import streamlit as st
from twilio.rest import Client

def send_sms(account_sid, auth_token, sender_phone_number, receiver_phone_number):
    # Message to be Sent
    message = 'Hey Where Are You?🤨...TUDU is missing you😕 come fast and complete your goals'

    # Initialize Twilio Client
    client = Client(account_sid, auth_token)

    # Send SMS
    client.messages.create(
        body=message,
        from_=sender_phone_number,
        to=receiver_phone_number
    )

    st.success("SMS sent successfully!")

def main():
    st.title("Twilio SMS Sender")

    # Load Twilio credentials from Streamlit secrets
    account_sid = st.secrets["twilio"]["account_sid"]
    auth_token = st.secrets["twilio"]["auth_token"]
    sender_phone_number = st.secrets["twilio"]["sender_phone_number"]
    receiver_phone_number = st.secrets["twilio"]["receiver_phone_number"]

    # Call the send_sms function directly
    send_sms(account_sid, auth_token, sender_phone_number, receiver_phone_number)

if __name__ == "__main__":
    main()
