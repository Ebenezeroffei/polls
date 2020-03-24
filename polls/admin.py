from django.contrib import admin
from .models import Question,Choice,Comment,CentralVotes

# Register your models here.

admin.site.register(Question)
admin.site.register(Choice)
admin.site.register(Comment)
admin.site.register(CentralVotes)