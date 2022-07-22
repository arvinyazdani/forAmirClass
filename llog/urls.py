from django.urls import path
from .views import topics, topic

app_name = "llog"

urlpatterns = [
    path('topics/', topics , name="topics"),
    path('topic/<int:topic_id>/', topic, name="topic"),
  
]