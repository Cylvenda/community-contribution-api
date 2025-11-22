from django.contrib import admin
from .models import Contributions, Contributors

class ContributionsAdmin(admin.ModelAdmin):
    list_display = ("id", "title", "targeted_user", "user")

class ContributorsAdmin(admin.ModelAdmin):
    list_display = ("id", "Contributions", "user", "amount", "payment_method")

admin.site.register(Contributions, ContributionsAdmin)
admin.site.register(Contributors, ContributorsAdmin)
