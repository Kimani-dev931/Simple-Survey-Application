# Generated by Django 4.2.7 on 2023-11-06 14:35

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleSurveyApp', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Response',
            new_name='SurveyResponse',
        ),
    ]
