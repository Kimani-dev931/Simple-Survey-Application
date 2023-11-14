from django.contrib import admin

# Register your models here.
from .models import Question, SurveyResponse,Choice

admin.site.register(Question)
#admin.site.register(Certificate)
admin.site.register(SurveyResponse)
admin.site.register(Choice)