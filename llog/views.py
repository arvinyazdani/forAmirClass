from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Topic


def get(request):
    topic = Topic.objects.all()
    return HttpResponse(f'topics : {topic[0]},{topic[1]},{topic[2]}')
