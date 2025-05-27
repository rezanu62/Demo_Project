from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import TrainingVideo, FAQ

@admin.register(TrainingVideo)
class TraningVideo(ModelAdmin):
    list_display = ("id", "title", "video")
    search_fields = ("id","titile")

@admin.register(FAQ)
class OptionAdmin(ModelAdmin):
    list_display = ("id", "question", "answer")
    search_fields = ("id","question")