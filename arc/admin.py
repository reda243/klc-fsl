from django.contrib import admin
from.models import logements
from.models import voitures
from.models import services
from.models import res

admin.site.register(logements)
admin.site.register(voitures)
admin.site.register(services)
admin.site.register(res)
