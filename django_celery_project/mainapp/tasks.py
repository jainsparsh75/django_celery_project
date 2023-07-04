

from django.contrib.auth import get_user_model
from celery import shared_task
from django.core.mail import send_mail
# from django_celery_project import settings

@shared_task(bind=True)
def test_func(self):
    #operations
    for i in range(10):
        print(i)
    return "Done"

@shared_task(bind=True)
def send_mail_func(self):
    print("inside send mail function")
    users = get_user_model().objects.all()
    for user in users:
        mail_subject = "Hi! Celery Testing"
        message = "celery beat scheduler is working fine"
        to_email = user.email
        send_mail(
            subject = mail_subject,
            message=message,
            from_email='jainsparsh75@gmail.com',
            recipient_list=[to_email],
            fail_silently=True,

        )
    return "mailsent"