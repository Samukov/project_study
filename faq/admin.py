from django.contrib import admin
from faq.models import *

class FAQAnswerTabularInline(admin.TabularInline):
    model = FAQAnswer
    extra = 1
    fk_name = 'question'

class FAQQuestionAdmin(admin.ModelAdmin):
    inlines = [FAQAnswerTabularInline]

admin.site.register(FAQQuestionCategory)
admin.site.register(FAQQuestion, FAQQuestionAdmin)
admin.site.register(FAQAnswer)
