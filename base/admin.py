import imp
from django.contrib import admin
# from matplotlib.style import use

# Register your models here.

from .models import Room, Topic , Message,AccessRecord,Webpage,Topic2,User2,UserProfileInfo

admin.site.register(Room)
admin.site.register(Topic)
admin.site.register(Message)
admin.site.register(AccessRecord)
admin.site.register(Webpage)
admin.site.register(Topic2)
admin.site.register(User2)
admin.site.register(UserProfileInfo)