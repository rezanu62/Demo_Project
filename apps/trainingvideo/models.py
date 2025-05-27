from django.db import models
from cloudinary.models import CloudinaryField

class TrainingVideo(models.Model):
    title = models.CharField(max_length=255)
    video = CloudinaryField("video", blank=True, null=True)

    def __str__(self):
        return self.title

class FAQ(models.Model):
    question = models.CharField(max_length=255)
    answer = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.question

