from django.db import models
from enum import Enum
import json

# Create your models here.

class QuestionType(Enum):
    CHOICE = 0
    TEXT = 1

class QuizModel(models.Model):
    author = models.ForeignKey('users.QuizUser', on_delete=models.CASCADE)
    users_completed = models.ForeignKey('users.UserResultModel', on_delete=models.CASCADE)
    date_created = models.DateField(default='2020-01-01')
    questions = models.TextField()

    def set_questions(self, x):
        self.questions = json.dumps(x)

    def get_questions(self):
        return json.loads(self.questions)