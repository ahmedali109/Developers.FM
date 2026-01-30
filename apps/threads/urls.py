from django.urls import path
from . import views

app_name = "threads"

urlpatterns = [
    path('ask-modal/', views.ask_question_modal, name='ask_modal'),
    path('reply/<int:question_id>/', views.add_reply, name='add_reply'),
    path('question/<int:question_id>/', views.question_detail, name='question_detail'),
    path('delete/<int:question_id>/', views.delete_question, name='delete_question'),
    path('questions/', views.question_list, name='question_list'),
]