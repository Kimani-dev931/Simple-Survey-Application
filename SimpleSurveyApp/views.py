from django.http import JsonResponse
from django.shortcuts import render, redirect
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, parser_classes
from rest_framework.views import APIView
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from .models import Question, SurveyResponse
from rest_framework.parsers import MultiPartParser, FormParser, JSONParser
from .serializers import QuestionSerializer, SurveyResponseSerializer
from django.http import HttpResponse
import django_filters.rest_framework
from rest_framework import generics
from django.contrib import messages
from rest_framework import filters
from django.template import loader
import requests
from django.db import models


@api_view(['GET'])
def question_view(request):
    try:
        questions = Question.objects.all()
    except Question.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = QuestionSerializer(questions, many=True)
        return Response(serializer.data)


def dynamicquestions(request):
    api_url = 'http://127.0.0.1:8000/api/questions/'

    try:
        response = requests.get(api_url)
        response.raise_for_status()
        questions = response.json()

        sorted_questions = sorted(questions, key=lambda x: x['id'])

    except requests.exceptions.RequestException as e:
        sorted_questions = []
        print(f"Error fetching questions: {e}")

    return render(request, 'Form.html', {'questions': sorted_questions})


class FormsubmitView(APIView):
    parser_classes = (MultiPartParser, FormParser)
    serializer_class = SurveyResponseSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return redirect('SimpleSurveyApp:success')

        return Response(
            serializer.errors,
            status=status.HTTP_400_BAD_REQUEST
        )


@api_view(['GET'])
def response_view(request):
    try:
        responses = SurveyResponse.objects.all()
    except SurveyResponse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = SurveyResponseSerializer(responses, many=True)
        return Response(serializer.data)


def dynamicresponses(request):
    api_url = 'http://127.0.0.1:8000/api/questions/response/'

    try:
        # Fetch responses from the DRF API
        response = requests.get(api_url)
        response.raise_for_status()
        responses = response.json()

        sorted_responses = sorted(responses, key=lambda x: x['id'])
        paginator = Paginator(sorted_responses, 3)
        page = request.GET.get('page')
        try:
            paginated_responses = paginator.page(page)
        except PageNotAnInteger:
            paginated_responses = paginator.page(1)
        except EmptyPage:
            paginated_responses = paginator.page(paginator.num_pages)
    except requests.exceptions.RequestException as e:

        paginated_responses = []
        print(f"Error fetching responses: {e}")

    return render(request, 'Response.html', {'responses': paginated_responses})


@api_view(['GET'])
def certificate_view(request, pk):
    try:
        survey_response = SurveyResponse.objects.get(pk=pk)
    except SurveyResponse.DoesNotExist:
        return Response({'detail': 'Certificate not found.'}, status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        if survey_response.my_certs:
            file_path = survey_response.my_certs.path
            with open(file_path, 'rb') as file:
                response = HttpResponse(file.read(), content_type='application/pdf')
                response['Content-Disposition'] = f'attachment; filename="{survey_response.my_certs.name}"'
                return response
        else:
            return Response({'detail': 'Certificate not found.'}, status=status.HTTP_404_NOT_FOUND)


class SearchListView(generics.ListAPIView):
    queryset = SurveyResponse.objects.all()
    serializer_class = SurveyResponseSerializer
    filter_backends = [django_filters.rest_framework.DjangoFilterBackend]
    filterset_fields = ['email_address']

    def get(self, request, *args, **kwargs):
        search_param = request.GET.get('search')

        if not search_param:
            return redirect('SimpleSurveyApp:feedback')
        queryset = self.queryset.filter(email_address__icontains=search_param)
        if not queryset.exists():
            return redirect('SimpleSurveyApp:error_page', search_param)

        serializer = self.get_serializer(queryset, many=True)
        context = {'responses': serializer.data, 'search_query': search_param}
        return render(request, 'Response.html', context)


def success_message(request):
    return render(request, 'Success.html')


def search_error(request, search_param):
    context = {
        'search_param': search_param,
    }
    return render(request, 'errorsearch.html', context)
