# Generated by Django 4.2.7 on 2023-11-12 09:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('SimpleSurveyApp', '0007_alter_certificate_certificate'),
    ]

    operations = [
        migrations.AlterField(
            model_name='certificate',
            name='certificate',
            field=models.FileField(upload_to='media'),
        ),
    ]
