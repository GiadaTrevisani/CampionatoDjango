from django.contrib import admin

# Register your models here.

from .models import Calendario

admin.site.register(Calendario)

from .models import Campionati

admin.site.register(Campionati)

from .models import Classifica

admin.site.register(Classifica)

from .models import Risultati

admin.site.register(Risultati)

from .models import Schedina

admin.site.register(Schedina)

from .models import Squadre

admin.site.register(Squadre)

from .models import Statistiche

admin.site.register(Statistiche)