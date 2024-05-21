from django.contrib import admin

from .models import General, Food, Breast, Sleep, Diaper, Hygiene, Medicine

# Register your models here.

admin.site.register(General)
admin.site.register(Food)
admin.site.register(Breast)
admin.site.register(Sleep)
admin.site.register(Diaper)
admin.site.register(Hygiene)
admin.site.register(Medicine)