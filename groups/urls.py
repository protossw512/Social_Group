from django.urls import path
from groups import views

app_name='groups'

urlpatterns = [
    url('', views.ListGroups.as_view(), name='all'),
    url('new/', views.CreateGroup.as_view(), name='create'),
    url('posts/in/<slug>/', views.SingleGroup.as_view(), name='single'),
]
