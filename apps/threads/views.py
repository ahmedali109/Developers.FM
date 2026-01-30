from django.shortcuts import render, redirect, get_object_or_404
from apps.threads.forms import QuestionForm, ReplyForm
from apps.threads.models import Question, Reply
from django.contrib.auth.decorators import login_required
from django.db.models import Count
from django.views.decorators.http import require_http_methods
from apps.accounts.models import User
from django.contrib import messages

@login_required
def profile(request):
    """Display user profile with all tabs data"""
    # Get messages from me
    messages_from_me = Question.objects.filter(
        sender=request.user
    ).order_by('-created_at')

    # Get messages to me
    messages_to_me = Question.objects.filter(
        receiver=request.user
    ).select_related('sender').order_by('-created_at')

    # Get feed (all questions with replies)
    feed = Question.objects.filter(
        sender__isnull=False
    ).select_related('sender').prefetch_related('replies__sender').order_by('-created_at')[:20]

    # Get all users except current user
    users = User.objects.exclude(id=request.user.id)[:20]

    form = QuestionForm()

    context = {
        'messages_from_me': messages_from_me,
        'messages_to_me': messages_to_me,
        'feed': feed,
        'users': users,
        'form': form,
    }

    return render(request, 'accounts/profile.html', context)


@login_required
def ask_question_modal(request):
    """Handle asking a new question via modal"""
    if request.method == "POST":
        form = QuestionForm(request.POST)
        print(f"DEBUG: Form valid: {form.is_valid()}")
        if form.is_valid():
            print(f"DEBUG: Form data - receiver: {form.cleaned_data.get('receiver')}, content: {form.cleaned_data.get('content')}")
            question = form.save(sender=request.user)
            print(f"DEBUG: Question created with sender: {question.sender}")
            messages.success(request, 'Question sent successfully!')
            return redirect('profile')
        else:
            print(f"DEBUG: Form errors: {form.errors}")
            messages.error(request, 'Failed to send question. Please try again.')
    
    return redirect('profile')


@login_required
@require_http_methods(["POST"])
def add_reply(request, question_id):
    """Add a reply to a question"""
    question = get_object_or_404(Question, id=question_id)
    form = ReplyForm(request.POST)
    
    if form.is_valid():
        reply = form.save(
            thread=question,
            sender=request.user,
            commit=True
        )
        messages.success(request, 'Reply added successfully!')
        
        # Update question status to answered
        if question.status == 'pending':
            question.status = 'answered'
            question.save(update_fields=['status'])
    else:
        messages.error(request, 'Failed to add reply. Please try again.')
    
    return redirect('profile')


@login_required
@require_http_methods(["POST"])
def increment_view_count(request, question_id):
    """Increment the view count for a question"""
    try:
        question = Question.objects.get(id=question_id)
        question.views_count += 1
        question.save(update_fields=['views_count'])
        return redirect('question_detail', pk=question_id)
    except Question.DoesNotExist:
        return redirect('profile')


@login_required
def question_list(request):
    """Display all questions with pagination"""
    questions = Question.objects.filter(
        sender__isnull=False
    ).select_related('sender', 'receiver').annotate(
        answers_count=Count('replies')
    ).order_by('-created_at')
    
    context = {
        'questions': questions,
    }
    
    return render(request, 'threads/question_list.html', context)


@login_required
def question_detail(request, question_id):
    """Display a single question with all its replies"""
    try:
        question = Question.objects.get(id=question_id)
        # Increment view count
        question.views_count += 1
        question.save(update_fields=['views_count'])
        
        # Get all replies for this question
        replies = question.replies.select_related('sender').order_by('created_at')
        
        context = {
            'question': question,
            'replies': replies,
        }
        
        return render(request, 'threads/question_detail.html', context)
    except Question.DoesNotExist:
        return redirect('profile')