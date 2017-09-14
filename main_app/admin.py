from django.contrib import admin
from .models import Team
from .models import Player
from .models import Venue
from .models import Match
from .models import Statistics
from .models import Enquiries
#from .models import Messages

# Register your models here.
admin.site.register(Team)
admin.site.register(Player)
admin.site.register(Venue)
admin.site.register(Match)
admin.site.register(Statistics)
admin.site.register(Enquiries)
#admin.site.register(Messages)

