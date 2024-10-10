from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import Practice

@receiver(post_save , sender = Practice)
def send_practice_email(sender , instance , created , **kwargs):
    if created:
        subject = f'new practice: {instance.question}'
        message = f'new practice with this question has been realised: {instance.question}'
        recipient_list = [instance.class_assigned.student]
        send_mail(subject , message , "maryaam.ki83@gmail.com" , recipient_list)
