"""定义learning_logs的URL模式"""
from django.urls import path
from . import views 

app_name = 'learning_logs'
urlpatterns = [
    #主页
    #使用path()
    path('',views.index,name = 'index'),
    # Page that shows all topics
    path('topic/',views.topics,name = 'topics'),
     # Detail page for a single topic.
    path('topic/<int:topic_id>/',views.topic,name = 'topic'),

]