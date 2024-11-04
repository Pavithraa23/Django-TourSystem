# tour/email_utils.py
from django.core.mail import send_mail
from django.conf import settings

def send_confirmation_email(user, tour_details):
    user_email = user.email  # Get the user's email

    subject = 'Booking Confirmation'
    message = f'Thank you for booking your tour! Here are the details:\n{tour_details}'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    try:
        send_mail(subject, message, email_from, recipient_list)
        print("Email sent successfully.")
    except Exception as e:
        print(f"Error sending email: {e}")
