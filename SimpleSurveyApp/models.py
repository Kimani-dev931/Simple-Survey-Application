from django.db import models

GENDER_CHOICES = [
    ('MALE', 'male'),
    ('FEMALE', 'female'),
    ('OTHER', 'other'),
]
PROGRAMMING_STACK_CHOICES = [
    ('REACT', 'React Js'),
    ('ANGULAR', 'Angular Js'),
    ('VUE', 'Vue Js'),
    ('SQL', 'Sql'),
    ('POSTGRES', 'Postgres'),
    ('MYSQL', 'Mysql'),
    ('JAVA', 'Java'),
    ('PHP', 'Php'),
    ('GO', 'Go'),
    ('RUST', 'Rust'),

]


class Question(models.Model):
    name = models.CharField(max_length=255)
    type = models.CharField(max_length=50)
    required = models.BooleanField(blank=False)
    text = models.TextField(max_length=300)
    description = models.TextField(max_length=255)


class Choice(models.Model):
    question = models.ForeignKey(Question, related_name='choices', on_delete=models.CASCADE)
    G_value = models.CharField(max_length=10, choices=GENDER_CHOICES, blank=True)
    PS_value = models.CharField(max_length=50, choices=PROGRAMMING_STACK_CHOICES, blank=True)


class SurveyResponse(models.Model):
    full_name = models.CharField(max_length=255)
    email_address = models.EmailField(max_length=30)
    description = models.TextField(max_length=500)
    gender = models.CharField(max_length=10, )
    programming_stack = models.CharField(max_length=20, blank=False)
    question = models.ForeignKey(Question, on_delete=models.CASCADE, null=True)
    date_responded = models.DateTimeField(auto_now_add=True)
    my_certs = models.FileField(blank=False)
