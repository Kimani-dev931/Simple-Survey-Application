# Generated by Django 4.2.7 on 2023-11-12 02:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleSurveyApp', '0005_alter_surveyresponse_question'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate',
            field=models.FileField(upload_to='certificates'),
        ),
    ]
