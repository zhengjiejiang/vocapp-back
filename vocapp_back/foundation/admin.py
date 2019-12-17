from django.contrib import admin

# Register your models here.
from .models import Vocabulary,Daily

admin.site.register(Vocabulary)
admin.site.register(Daily)
