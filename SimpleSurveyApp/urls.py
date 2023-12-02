from django.urls import path

from .views import question_view, response_view, FormsubmitView, certificate_view,SearchListView
from . import views

app_name = 'SimpleSurveyApp'

urlpatterns = [
    path('', views.dynamicquestions, name='home'),
    path('responses/', views.dynamicresponses, name='feedback'),
    path('api/questions/', question_view, name='question-list'),
    path('api/questions/response/', response_view, name='fetch-responses'),
    path('api/questions/responses/', FormsubmitView.as_view(), name='submit-responses'),
    path('api/questions/responses/certificates/<int:pk>/',certificate_view, name='certificate-list'),
    path('search/', SearchListView.as_view(), name='search-list'),
    path('successful/', views.success_message, name='success'),
    path('error/<str:search_param>/', views.search_error, name='error_page'),

]
