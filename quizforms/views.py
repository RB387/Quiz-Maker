from django.shortcuts import render, redirect, Http404, reverse, HttpResponse
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
        try:
            data = request.body.decode('utf-8')
            QuizModel().question_serialize(data) #try to serialize to check if JSON is okay
            json_data = json.loads(data)
            quiz = QuizModel.objects.create(author=request.user, questions=json_data,
                                        date_created=datetime.datetime.now().strftime('%Y-%m-%d'))
        except:
            return HttpResponseBadRequest(
                json.dumps({'message': 'Quiz data is incorrect, please fill all fields'}),
                content_type="application/json")
        return HttpResponse(json.dumps({'url': reverse('quiz', kwargs={'pk':quiz.pk})}), content_type="application/json")
    return render(request, 'create_quiz.html')

def quiz_view(request, pk):
    try:
        quiz = QuizModel.objects.get(pk=pk)
    except QuizModel.DoesNotExist:
        raise Http404
    quiz_list = QuizModel().question_serialize(quiz.questions)
    forms = []
    for quiz_data in quiz_list:
        forms.append(QuizForm(question=quiz_data.question, answer=quiz_data.answer,
                              q_type=quiz_data.q_type, choices=zip(range(len(quiz_data.choices)), quiz_data.choices)))
    return render(request, 'question.html', {'forms': forms})
