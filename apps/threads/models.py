from django.db import models
from apps.accounts.models import User

class Question(models.Model):
    sender = models.ForeignKey(User, null=True,on_delete=models.CASCADE, related_name="sent_questions")
    receiver = models.ForeignKey(User, null=True,on_delete=models.CASCADE, related_name="received_questions")
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
    created_at = models.DateTimeField(auto_now_add=True)



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

    def __str__(self):
        return f"Reply by {self.sender} on Question #{self.thread.id}"