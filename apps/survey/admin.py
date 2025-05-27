from django.contrib import admin
from unfold.admin import ModelAdmin
from .models import Option, SurveyUser, Survey



@admin.register(Option)
class OptionAdmin(ModelAdmin):
    list_display = ('id', 'text')
    search_fields = ('text',)


@admin.register(SurveyUser)
class SurveyUserAdmin(ModelAdmin):
    list_display = ('id', 'first_name', 'last_name', 'email', 'company_name', 'created_at', 'updated_at')
    search_fields = ('first_name', 'last_name', 'email', 'company_name')
    list_filter = ('created_at', 'updated_at')
    ordering = ('-created_at',)


@admin.register(Survey)
class SurveyAdmin(ModelAdmin):
    list_display = ('id', 'question', 'user')
    search_fields = ('question', 'user__first_name', 'user__last_name', 'user__email')
    list_filter = ('user',)
    filter_horizontal = ('options',)  # Useful UI for many-to-many fields




