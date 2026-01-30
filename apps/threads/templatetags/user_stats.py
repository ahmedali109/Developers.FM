from django import template
from apps.threads.models import Question, Reply

register = template.Library()


@register.filter
def questions_count(user):
    """Count questions sent by a user"""
    return Question.objects.filter(sender=user).count()


@register.filter
def answers_count(user):
    """Count replies sent by a user"""
    return Reply.objects.filter(sender=user).count()


@register.filter
def reply_count(question):
    """Count replies for a question"""
    return question.replies.count()
