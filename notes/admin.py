from django.contrib import admin
from django.db import models
from .models import Note
from .models import PersonalNote
from django.contrib.auth.models import User
class NoteAdmin(admin.ModelAdmin):
	readonly_fields=('created_at', 'last_modified')

# Register your models here.
admin.site.register(Note, NoteAdmin)
# Register your models here.
admin.site.register(PersonalNote)   # etc.

