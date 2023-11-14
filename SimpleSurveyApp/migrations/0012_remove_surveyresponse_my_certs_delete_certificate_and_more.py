# Generated by Django 4.2.7 on 2023-11-12 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleSurveyApp', '0011_alter_certificate_certificate'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='surveyresponse',
            name='my_certs',
        ),
        migrations.DeleteModel(
            name='Certificate',
        ),
        migrations.AddField(
            model_name='surveyresponse',
            name='my_certs',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
