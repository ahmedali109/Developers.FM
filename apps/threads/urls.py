from django.urls import path
from . import views

app_name = "threads"

urlpatterns = [
     path('ask-modal/', views.ask_question_modal, name='ask_modal'),
]
