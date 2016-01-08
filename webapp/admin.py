from django.contrib import admin

# Register your models here.

from .models import Fgroup
from .models import Team
from .models import Series
from .models import Round
from .models import Emailround
from .models import Payment
from .models import Prediction
from .models import Nilnils

admin.site.register(Fgroup)
admin.site.register(Team)
admin.site.register(Series)
admin.site.register(Round)
admin.site.register(Emailround)
admin.site.register(Payment)
admin.site.register(Prediction)
admin.site.register(Nilnils)


