from django.db import models

class Option(models.Model):
    text = models.CharField(max_length=255)

    def __str__(self):
        return self.text


class SurveyUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    company_name = models.CharField(max_length=100)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    # image_field = models.ImageField(upload_to='user_images/', blank=True, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Survey(models.Model):
    user = models.ForeignKey(SurveyUser, on_delete=models.CASCADE, related_name='surveys')  
    question = models.CharField(max_length=255)  
    options = models.ManyToManyField(Option, related_name='surveys')

    def __str__(self):
        return self.question
