
from django.urls import path
from core import views




urlpatterns = [
    path('', views.home,name='home'),
    path('update/<todo>/', views.update,name='update'),
    path('delete/<todo>', views.delete,name='delete'),
]


