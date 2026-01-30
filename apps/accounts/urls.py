from django.urls import path
from .views import register_view, login_view, logout_view, profile_view
from apps.threads import views as thread_views

urlpatterns = [
    path('register/', register_view, name='register'),
    path('login/', login_view, name='login'),
    path('logout/', logout_view, name='logout'),
    path('profile/', thread_views.profile, name='profile')
]
