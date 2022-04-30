from django.contrib import admin
from django.contrib.auth.models import Group, User
from django.contrib.auth.admin import UserAdmin

from .models import Account

# Register your models here.


class AccountInLine(admin.StackedInline):
  model = Account


class CustomizedUserAdmin (UserAdmin):
  inlines = (AccountInLine,)


admin.site.unregister(Group)
admin.site.unregister(User)

admin.site.register(User, CustomizedUserAdmin)
admin.site.register(Account)
