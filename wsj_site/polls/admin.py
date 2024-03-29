from django.contrib import admin

from .models import Question, Choice

#admin.site.register(Question)

class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        (None,                  {'fields': ['question_text']}),
        ('Date information',    {'fields': ['pub_date']}), 
    ]
    inlines = [ChoiceInline]
    search_fields = ['question_text']
    list_filter = ['pub_date']
    list_display = ('question_text', 'pub_date', 'was_published_recently')    

admin.site.register(Question, QuestionAdmin)

# Register your models here.
