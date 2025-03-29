from django.contrib import admin
from .models import Ledger, Passbook

@admin.register(Ledger)
class LedgerAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ledger._meta.fields]
    search_fields = ('name','type',) 
    list_filter = ('created_at',)  

@admin.register(Passbook)
class PassbookAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Passbook._meta.fields]
    search_fields = ('bank_name',) 
    list_filter = ('created_at',) 