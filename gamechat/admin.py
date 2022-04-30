from django.contrib import admin
from .models import User, Message, Role

# Register your models here.


class UserAdmin(admin.ModelAdmin):
  list_display = ('username', 'date_of_reg')


class MessageAdmin(admin.ModelAdmin):
  list_display = ('username', 'text', 'date')


admin.site.register(User, UserAdmin)
admin.site.register(Message, MessageAdmin)
admin.site.register(Role)
