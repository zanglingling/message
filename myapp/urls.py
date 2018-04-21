from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^main/$', views.Main.as_view(), name='main'),

]
