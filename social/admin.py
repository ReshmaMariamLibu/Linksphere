from django.contrib import admin

# Register your models here.

from social.models import Stories,Posts

admin.site.register(Stories)
admin.site.register(Posts)


#python manage.py createsuperuser