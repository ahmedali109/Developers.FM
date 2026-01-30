from django import forms
from apps.threads.models import Question

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
        # Always save the sender to track who asked
        question.sender = sender
        # Save whether it was asked anonymously
        question.is_anonymous = self.cleaned_data.get('ask_anonymously', False)
        if commit:
            question.save()
        return question
