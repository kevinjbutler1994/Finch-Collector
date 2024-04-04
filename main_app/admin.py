from django.contrib import admin
# add Feeding to the import
from .models import Finch, Feeding, Toy

admin.site.register(Finch)
admin.site.register(Toy) 
admin.site.register(Feeding)
