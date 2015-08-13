from django.contrib import admin

from .models import PlayerCharacter
from .models import PCValue
from .models import *
# from .models import *

admin.site.register(PlayerCharacter)
admin.site.register(PCValue)
admin.site.register(Abilities)
admin.site.register(AbilityValues)


# Register your models here.
