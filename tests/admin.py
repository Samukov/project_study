from django.contrib import admin

from tests.models import *

class VariantInline(admin.TabularInline):
    model = TestVariant
    fk_name = 'test_question'
    extra = 4


class TestQuestionAdmin(admin.ModelAdmin):
    inlines = [VariantInline]


admin.site.register(FinalTest)
admin.site.register(TestQuestion, TestQuestionAdmin)
admin.site.register(TestVariant)
admin.site.register(FinalExamResult)


