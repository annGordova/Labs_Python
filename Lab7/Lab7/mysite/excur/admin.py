from django.contrib import admin

# Register your models here.
from .models import Client, Destination, Guide, Excursion_template, Excursion_client

admin.site.register(Client)
admin.site.register(Destination)
admin.site.register(Guide)
admin.site.register(Excursion_template)
admin.site.register(Excursion_client)
