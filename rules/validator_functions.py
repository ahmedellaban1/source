import random
from django.core.mail import send_mail
from django.conf import settings


number_digit = 6
min_value = 6 ** (number_digit - 1)
max_value = (6 ** number_digit) - 1

def verification_code(email):
    random_number = random.randint(min_value, max_value)
    print("*********************>",random_number)
    subject = 'AVIATO | VERFY YOUR EMAIL'
    send_mail(
        subject,
        f'your verification_code is {random_number} \n don\'t shere code with anyone',
        f'ellaban285@gamil.com',
        settings.EMAIL_HOST_USER,
        [email]
        )
    return f'{random_number}'
