from django.core.mail import send_mail
from django.conf import settings

def send_email(username,email):
    subject = "Welcome to FASCO"
    body = f'''
                Hello {username}! your registration has been completed,
                do reach out to our dev team for further information.
                For any complains, kindly reach out to our customer rep.

            '''
    send_mail(
    subject,
    body,
    settings.EMAIL_HOST_USER,
    [email],
    fail_silently=False,
)