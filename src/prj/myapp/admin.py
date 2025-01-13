from django.contrib import admin

from .models.module import *
from .models.schedule import *

# Register your models here.
admin.site.register(Module)
admin.site.register(Schedule)