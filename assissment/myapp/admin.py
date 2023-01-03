from django.contrib import admin
from myapp.models import *
# Register your models here.

admin.site.register(productMainModel)
admin.site.register(productColourModel)
admin.site.register(productImageModel)