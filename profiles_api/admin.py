from django.contrib import admin
from profiles_api import models

# Register model accessible to admin interface
admin.site.register(models.UserProfile)
