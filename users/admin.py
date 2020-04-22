from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .forms import QuizUserChangeForm, QuizUserCreationForm
from .models import QuizUser

# Register your models here.
class QuizUserAdmin(UserAdmin):
    add_form = QuizUserCreationForm
    form = QuizUserChangeForm
    model = QuizUser

admin.site.register(QuizUser, QuizUserAdmin)