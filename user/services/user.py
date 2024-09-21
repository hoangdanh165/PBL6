from django.core import signing
from django.core.mail import send_mail
from django.conf import settings
from django.core.mail import EmailMultiAlternatives
from django.template.loader import render_to_string
from django.utils.html import strip_tags


def generate_email_verification_token(user):
    print('token generated')
    return signing.dumps({'user_id': user.id}, salt='email-verification-salt')

def verify_email_verification_token(token):
    try:
        data = signing.loads(token, salt='email-verification-salt', max_age=3600)  
        return data['user_id']
    except signing.SignatureExpired:
        return None  
    except signing.BadSignature:
        return None  

# def send_verification_email(user):
#     token = generate_email_verification_token(user)
#     verify_url = f"http://127.0.0.1:8000/verify-email/?token={token}"  
#     send_mail(
#         'Verify your email',
#         f'Click the link to verify your email: {verify_url}',
#         settings.DEFAULT_FROM_EMAIL,
#         [user.email],
#         fail_silently=False,
#     )



def send_verification_email(user):
    token = generate_email_verification_token(user)
    subject = 'Xác nhận email của bạn'

    default_host = settings.DEFAULT_HOST
    default_scheme = (
        "http"
        if default_host.startswith("localhost") or default_host.startswith("127.0.0.1")
        else "https"
    )
    # logo = f"{default_scheme}://{default_host}/static/user/email/logo.svg"

    logo = 'static/user/email/logo.svg'
    
    verification_url = f'{ default_scheme }://{ default_host }/api/v1/users/verify-email?token={token}'

    html_content = render_to_string('user/email/email_verification.html', {
        'verification_url': verification_url,
        'logo_url': logo
        # Add expired time
        # Add hello username
    })
    
    text_content = strip_tags(html_content)  
    text_content += f'\n\nXác nhận email: {verification_url}'  

    email = EmailMultiAlternatives(subject, text_content, settings.DEFAULT_FROM_EMAIL, [user.email])
    email.attach_alternative(html_content, "text/html")  
    email.send()
