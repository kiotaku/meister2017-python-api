from django.shortcuts import render
from django.http import HttpResponse
from .models import Count

def index(req):
    count = Count.objects.get(id=1)
    count.count += 1
    count.save()
    return HttpResponse('Hello World! Access Count: {}'.format(count.count))

# Create your views here.
