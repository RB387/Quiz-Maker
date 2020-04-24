from django import forms
from .models import QuestionType

class QuizForm(forms.Form):
    def __init__(self, question, answer, q_type, choices, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if q_type == QuestionType.CHOICE.value:
            self.fields['answers'] = forms.ChoiceField(choices=choices, widget=forms.RadioSelect)
        elif q_type == QuestionType.TEXT.value:
            self.fields['answers'] = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control'}))
        self.answer = answer
        self.question = question