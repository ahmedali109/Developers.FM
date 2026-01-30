from django import forms
from apps.threads.models import Question, Reply

class QuestionForm(forms.ModelForm):
    ask_anonymously = forms.BooleanField(required=False)

    class Meta:
        model = Question
        fields = ['receiver', 'content']
        widgets = {
            'content': forms.Textarea(attrs={'placeholder': 'What would you like to ask?'}),
        }

    def save(self, sender=None, commit=True):
        question = super().save(commit=False)
        question.sender = sender
        question.is_anonymous = self.cleaned_data.get('ask_anonymously', False)
        print(f"DEBUG: Saving question - sender: {sender}, is_anonymous: {question.is_anonymous}, receiver: {question.receiver}")
        if commit:
            question.save()
            print(f"DEBUG: Question saved with ID: {question.id}")
        return question


class ReplyForm(forms.ModelForm):
    class Meta:
        model = Reply
        fields = ['content']
        widgets = {
            'content': forms.Textarea(attrs={
                'placeholder': 'Write your reply...',
                'rows': 2
            }),
        }

    def save(self, thread=None, sender=None, parent=None, commit=True):
        reply = super().save(commit=False)
        reply.thread = thread
        reply.sender = sender
        if parent:
            reply.parent = parent
        if commit:
            reply.save()
        return reply