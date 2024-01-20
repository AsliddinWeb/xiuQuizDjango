from django.contrib import admin

from .models import *

admin.site.register(Subject)

class AnswerInline(admin.TabularInline):
    model = Answer
class QuestionAdmin(admin.ModelAdmin):
    inlines = [AnswerInline]
    list_display = ('text', 'quiz')
admin.site.register(Question, QuestionAdmin)

class AnswerAdmin(admin.ModelAdmin):
    list_display = ('text', 'question', 'is_correct')
admin.site.register(Answer, AnswerAdmin)

admin.site.register(QuizType)

class QuizAdmin(admin.ModelAdmin):
    list_display = ('title', 'start_time', 'end_time', 'deadline', 'max_questions', 'subject',
                    'maximum_attempts', 'status')
    filter_vertical = ('groups', 'no_permission_students')
admin.site.register(Quiz, QuizAdmin)

class UserAskedAnswerAdmin(admin.ModelAdmin):
    list_display = ('quiz', 'user', 'question', 'chosen_answer')
admin.site.register(UserAskedAnswer, UserAskedAnswerAdmin)

class ResultAdmin(admin.ModelAdmin):
    list_display = ('student', 'quiz', 'score', 'start_time', 'end_time')
admin.site.register(Result, ResultAdmin)
