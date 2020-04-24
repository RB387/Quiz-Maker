from django.urls import path
from .views import home_page_view, quiz_add_view, quiz_view

urlpatterns = [
    path('', home_page_view, name='home'),
    path('add_quiz/', quiz_add_view, name='add_quiz'),
    path('quiz/<int:pk>/', quiz_view, name='quiz')
]