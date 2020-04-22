from django.db import models
from django.contrib.auth.models import AbstractUser
import json

class UserResultModel(models.Model):
    user = models.ForeignKey('users.QuizUser', on_delete=models.CASCADE)
    result = models.TextField()
    answers = models.TextField()
    time = models.CharField(max_length=100)

    def set_answers(self, x):
        self.questions = json.dumps(x)

    def get_answers(self):
        return json.loads(self.questions)

class QuizUser(AbstractUser):
    join_date = models.DateField(default='2020-01-01')