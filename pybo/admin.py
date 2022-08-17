from django.contrib import admin
from .models import Question


class QeustionAdmin(admin.ModelAdmin):
    search_fields = ['subject']


admin.site.register(Question, QeustionAdmin)
