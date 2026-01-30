from django.shortcuts import render, redirect
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth import get_user_model
from .forms import UserRegisterForm, UserLoginForm
from apps.threads.models import Question

User = get_user_model()

# Register view
def register_view(request):
    if request.method == 'POST':
        form = UserRegisterForm(request.POST, request.FILES)
        if form.is_valid():
            user = form.save()
            login(request, user)  
            return redirect('profile')
    else:
        form = UserRegisterForm()
    return render(request, 'accounts/register.html', {'form': form})


# Login view
def login_view(request):
    if request.method == 'POST':
        form = UserLoginForm(request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            login(request, user)
            return redirect('profile')
    else:
        form = UserLoginForm()
    return render(request, 'accounts/login.html', {'form': form})


# Logout view
def logout_view(request):
    logout(request)
    return redirect('login')


# Profile view
@login_required(login_url='login')
def profile_view(request):
    user = request.user
    
    # Fetch all users except the current user, ordered by date joined
    all_users = User.objects.exclude(id=user.id).order_by('-date_joined')[:20]
    
    # Add real question and answer counts to each user
    users_with_stats = []
    for user_obj in all_users:
        # Count questions sent by this user (excluding null senders)
        user_obj.questions_count = Question.objects.filter(sender=user_obj, sender__isnull=False).count()
        # Count replies/answers made by this user
        user_obj.answers_count = Question.objects.filter(replies__sender=user_obj).distinct().count()
        users_with_stats.append(user_obj)
    
    # Fetch questions sent by current user
    messages_from_me = Question.objects.filter(sender=user).order_by('-created_at')
    
    # Fetch questions received by current user
    messages_to_me = Question.objects.filter(receiver=user).order_by('-created_at')
    
    # Fetch feed - latest questions from all users, exclude null senders
    feed = Question.objects.filter(sender__isnull=False).order_by('-created_at')[:20]
    
    context = {
        'user': user,
        'messages_from_me': messages_from_me,
        'messages_to_me': messages_to_me,
        'feed': feed,
        'users': users_with_stats,
    }
    
    return render(request, 'accounts/profile.html', context)
