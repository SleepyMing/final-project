import random
import string
from users.models import EmailVerifyRecord
from django.core.mail import send_mail



def random_str(random_length=8):
    """generate 8 bit random string"""
    chars = string.ascii_letters + string.digits
    strcode = ''.join(random.sample(chars, random_length))
    return strcode

#Save the verification code and send the link with the verification code
def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    code  = random_str()
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    #After the verification code is saved, 
    #we will send the link with the verification code to the email address during registration!
    if send_type == 'register':
        email_title = 'LIG registration activation link'
        email_body = 'Please click the link below to activate your account: http://127.0.0.1:8000/users/active/{0}'.format(code)

        send_status = send_mail(email_title, email_body, 'sleepy_bear0326@163.com', [email])
        if send_status:
            pass

    elif send_type == 'forget':
        email_title = 'forget password'
        email_body = 'Please click the link below to change your password: http://127.0.0.1:8000/users/reset_pwd/{0}'.format(code)

        send_status = send_mail(email_title, email_body, 'sleepy_bear0326@163.com', [email])
        if send_status:
            pass
