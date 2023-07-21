from django.contrib import admin
from imdb_drf_app.models import *

# Register your models here.

admin.site.register(StreamPlatform)
admin.site.register(Watch)
admin.site.register(Review)