from django.urls import path

from . import views

app_name = 'polls'


urlpatterns = [
    # ex: /polls/
    path('', views.index, name='index'),
    # ex: /specifics/polls/5/
    # href="{% url 'polls:detail' question.id %}"
    path('<int:question_id>/', views.detail, name='detail'),

    # ex: /specifics/polls/5/
    # href="{% url 'detail' question.id %}"
    # path('specifics/<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/
    # href="/polls/{{ question.id }}/"
    #path('<int:question_id>/', views.detail, name='detail'),

    # ex: /polls/5/results/
    path('<int:question_id>/results/', views.results, name='results'),
    # ex: /polls/5/vote/
    path('<int:question_id>/vote/', views.vote, name='vote'),
]