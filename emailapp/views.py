from django.shortcuts import render
from django.views import View
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random
import requests
class Home(View):
    def get(self,request):
        return render(request,'input.html')
class send(View):
    def get(self,request):
        subject='Thank you for contacting us'
        otp = str(random.randint(10000000,999999999))
        print(otp)
        From_mail=settings.EMAIL_HOST_USER
        email=request.GET["t1"]
        mobno="+91"+request.GET["t2"]
        to_list=[email]
        send_mail(subject, otp, From_mail, to_list, fail_silently=False)
        resp=requests.post('https://textbelt.com/text',{
            'phone':mobno,
            'message':otp,
            'key':'2009d3f7036ac95ba3f597ef8f4c6c5d8cfc17ae2wO8OgtNdx4L8oolZQcCYonko'
        })
        return HttpResponse("mail sent successfully")

# Create your views here.
