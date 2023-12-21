from django.contrib import admin
from .models import user_info,temporary_user_info

admin.site.register(user_info)
admin.site.register(temporary_user_info)