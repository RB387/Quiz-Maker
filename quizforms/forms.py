from django import forms

class QuizForm(forms.Form):
    def __init__(self, questions, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['answers'] = forms.ChoiceField(choices=questions, widget=forms.RadioSelect)