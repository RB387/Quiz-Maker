from django.contrib.auth.forms import UserCreationForm, UserChangeForm, AuthenticationForm
from .models import QuizUser
from django import forms

class QuizUserCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = QuizUser
        fields = UserCreationForm.Meta.fields + ('join_date',)

class QuizUserChangeForm(UserChangeForm):
    class Meta(UserChangeForm.Meta):
        model = QuizUser
        fields = UserChangeForm.Meta.fields