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
        if sender and not self.cleaned_data.get('ask_anonymously', False):
            question.sender = sender
        else:
            question.sender = None 
        if commit:
            question.save()
        return question
