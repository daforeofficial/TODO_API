from celery import shared_task
from django.core.mail import send_mail
from django.utils import timezone
from .models import Task

@shared_task
def send_task_reminders():
    upcoming_tasks = Task.objects.filter(deadline__lt=timezone.now() + timezone.timedelta(days=1), is_completed=False)
    for task in upcoming_tasks:
        send_mail(
            f'Task Reminder: {task.title}',
            f'You have a task "{task.title}" due soon.',
            'from: Muzammil Aslam',
            [task.user.email],
            fail_silently=False,
        )

#function ko run krny k leay hr ghanty k bad
CELERY_BEAT_SCHEDULE = {
    'send-reminder-every-hour': {
        'task': 'tasks.tasks.send_task_reminders',
        'schedule': 3600.0,
    },
}