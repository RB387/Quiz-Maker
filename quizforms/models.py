from django.db import models
from enum import Enum
import json

# Create your models here.

class QuestionType(Enum):
    TEXT = '0'
    CHOICE = '1'

class BadJSON(Exception): pass

class Question:
    def __init__(self, question, answer, q_type, choices=[]):
        self.question = question
        self.answer = answer
        self.q_type = q_type
        self.choices = choices

    def __str__(self):
        outline = '<Question Object>\n'
        outline += f' - question: {self.question}\n'
        outline += f' - answer: {self.answer}\n'
        outline += f' - q_type: {self.q_type}\n'
        outline += f' - choices: {self.choices}\n'
        return outline

class QuizModel(models.Model):
    author = models.ForeignKey('users.QuizUser', on_delete=models.CASCADE)
    date_created = models.DateField(default='2020-01-01')
    questions = models.TextField()

    def question_serialize(self, data):
        questions = []
        data = json.loads(data.replace("'", '"'))
        for question_json in data.values():
            try:
                q_type = question_json['type']
                question = question_json['question']
                answer = question_json['answer']
                assert answer!=''
                if q_type == QuestionType.CHOICE.value:
                    choices = question_json['choices']
                    for choice in choices:
                        assert choice!=''
                else:
                    choices = []
                questions.append(Question(question=question, answer=answer, q_type=q_type, choices=choices))
            except:
                raise BadJSON()
        return questions

    def set_questions(self, x):
        self.questions = json.dumps(x)