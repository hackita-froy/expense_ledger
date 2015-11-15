from django.contrib import admin

# Register your models here.
from .models import Expense
from users.models import User

admin.site.register(Expense)
admin.site.register(User)
