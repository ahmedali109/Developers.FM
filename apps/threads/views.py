from django.shortcuts import render, redirect
from apps.threads.forms import QuestionForm
from apps.threads.models import Question
from django.contrib.auth.decorators import login_required
from django.db.models import Count

@login_required
def ask_question_modal(request):
    if request.method == "POST":
        form = QuestionForm(request.POST)
        if form.is_valid():
            form.save(sender=request.user)
            return redirect('profile') 
    else:
        form = QuestionForm()

    messages_from_me = Question.objects.filter(
        sender=request.user
    ).annotate(
        answers_count=Count('replies')
    ).order_by('-created_at')

    print(f"Number of questions: {messages_from_me.count()}")  

    context = {
        'form': form,
        'messages_from_me': messages_from_me,
    }

    return render(request, 'accounts/profile.html', context)