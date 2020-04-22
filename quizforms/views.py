from django.shortcuts import render, redirect, reverse
from .models import QuizModel
from .forms import QuizForm
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponseBadRequest
import json
import datetime
# Create your views here.
def home_page_view(request):
    if request.method == "POST":
        print(request.POST)
    return render(request, 'home.html')

@csrf_exempt
def quiz_add_view(request):
    if not request.user.is_authenticated: return redirect('/')
    if request.is_ajax():
        #try:
        json_data = json.loads(request.body)
        QuizModel.objects.create(author=request.user.pk, questions=json_data, date_created=datetime.datetime.now().strftime('%Y-%m-%d'))
        print(QuizModel.objects.all())
        #except:
            #return HttpResponseBadRequest('Bad JSON')
    return render(request, 'create_quiz.html')

def quiz_view(request, pk):
    pass