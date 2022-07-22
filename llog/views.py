from ast import Return
from django.shortcuts import render
from django.http import HttpResponse
from django.views import View
from .models import Topic


def topics(request):
    topic = Topic.objects.all()
    context = {"topics":topic}
    return render(request=request, template_name="llog/home.html", context=context)


def topic(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entry = topic.entry_set.all()
    context = {
        "entry":entry,
        "topic":topic
    }
    
    return render(request , "llog/topic.html", context)
    
