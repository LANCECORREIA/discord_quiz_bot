from django.contrib import admin

from .models import Answer, Question

# Register your models here.


class AnswerInline(admin.TabularInline):
    model = Answer
    fields = [
        "answer",
        "is_correct",
    ]


@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    fields = [
        "title",
        "points",
        "difficulty",
    ]
    list_display = [
        "title",
        "updated_at",
    ]
    inlines = [
        AnswerInline,
    ]
