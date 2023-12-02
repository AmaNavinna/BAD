from django.contrib import admin
from .models import NowShowingMovie, UpcomingMovie,Reg, Transaction
from main.models import Contact

# Register your models here.
admin.site.register(NowShowingMovie)
admin.site.register(UpcomingMovie)
admin.site.register(Reg)


class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'email', 'message')  # Display these fields in the admin list view

admin.site.register(Contact, ContactAdmin)

class TransactionAdmin(admin.ModelAdmin):
    list_display = ('user_name', 'email', 'movie', 'date', 'show_time')  # Display these fields in the admin list view

admin.site.register(Transaction, TransactionAdmin)