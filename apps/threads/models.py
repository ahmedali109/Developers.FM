from django.db import models
from apps.accounts.models import User

class Question(models.Model):
    sender = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="sent_questions")
    receiver = models.ForeignKey(User, null=True, on_delete=models.CASCADE, related_name="received_questions")
    title = models.CharField(max_length=255, default="Untitled Question")
    content = models.TextField()
    is_anonymous = models.BooleanField(default=False)
    status = models.CharField(
        max_length=20,
        choices=[
            ("pending", "Pending"),
            ("answered", "Answered"),
        ],
        default="pending"
    )
    views_count = models.IntegerField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created_at']
        verbose_name = 'Question'
        verbose_name_plural = 'Questions'

    def __str__(self):
        return f"{self.title} - {self.sender}"

    @property
    def replies_count(self):
        return self.replies.count()


class Reply(models.Model):
    thread = models.ForeignKey(
        Question, 
        on_delete=models.CASCADE, 
        related_name="replies"
    )
    parent = models.ForeignKey(
        "self", 
        null=True, 
        blank=True, 
        on_delete=models.CASCADE, 
        related_name="children"
    )
    sender = models.ForeignKey(
        User, 
        on_delete=models.CASCADE, 
        related_name="replies"
    )
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['created_at']
        verbose_name = 'Reply'
        verbose_name_plural = 'Replies'

    def __str__(self):
        return f"Reply by {self.sender} on Question #{self.thread.id}"