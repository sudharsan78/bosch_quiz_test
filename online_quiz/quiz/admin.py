from django.contrib import admin

from .models import Quiz, Questions, Choice

admin.site.register(Quiz)


class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 3


# admin.site.register(Choice)

class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]


admin.site.register(Questions, QuestionAdmin)



