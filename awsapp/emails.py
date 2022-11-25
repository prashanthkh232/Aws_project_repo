from django.core.mail import send_mail
import random
from django.conf import settings

def otp_send(email):
    subject="Email verification"
    otp=random.randint(100000,999999)
    message=f'Otp for verification is {otp}'
    email_from=settings.EMAIL_HOST
    send_mail(subject,message,email_from,[email])
    return otp