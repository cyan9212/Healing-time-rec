from django.contrib import admin

from .models import Review
from .models import Shop

admin.site.register(Shop)
admin.site.register(Review)

