from django.http.response import HttpResponse
from django.shortcuts import render
from .tasks import test_func,send_mail_func
from django_celery_beat.models import PeriodicTask, CrontabSchedule
from rest_framework.response import Response
from rest_framework.decorators import api_view
import json

# Create your views here.
def test(request):
    test_func.delay()
    return HttpResponse("your task will be done soon")

# Create your views here.
def send_mail_to_all(request):
    print("inside send mail to all")
    send_mail_func.delay()
    return HttpResponse("Sent")

# dynamic scheduling of tasks
@api_view(['GET'])
def schedule_mail(request):
    data = request.data
    schedule1, created = CrontabSchedule.objects.get_or_create(hour = int(data['hour']), minute = int(data['min']))
    task = PeriodicTask.objects.create(crontab=schedule1, task='mainapp.tasks.send_mail_func')#, args = json.dumps([[2,3]]))
    return Response({"successful": True})