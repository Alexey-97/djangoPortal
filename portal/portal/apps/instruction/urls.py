from django.urls import path
from . import views

app_name = 'instruction'
urlpatterns = [
    path('', views.index, name='instruction'),
    path('<int:instruction_id>/', views.detail, name='detail')
]
