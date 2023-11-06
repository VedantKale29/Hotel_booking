from django.contrib import admin
from .models import  Record,Hotel,Orders,HotelImages

# Register your models here.

admin.site.register(Hotel)
admin.site.register(Record)
admin.site.register(Orders)
admin.site.register(HotelImages)