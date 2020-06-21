from django.contrib import admin

# Register your models here.

from .models import Campionato

admin.site.register(Campionato)

from .models import Giornata

admin.site.register(Giornata)

from .models import Squadra

admin.site.register(Squadra)

from .models import Partita

admin.site.register(Partita)