from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),  # Home page of the polls app
    path('<int:question_id>/', views.detail, name='detail'),  # Detail page for a specific question
    path('<int:question_id>/results/', views.results, name='results'),
    path('<int:question_id>/vote/', views.vote, name='vote'),
]


