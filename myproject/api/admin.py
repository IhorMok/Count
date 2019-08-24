from django.contrib import admin
from .models import AccountantRecord


@admin.register(AccountantRecord)
class AccountantRecordAdmin(admin.ModelAdmin):
    list_display = ('date', 'created_at', 'updated_at', 'group', 'subgroup', 'amount')
#admin.site.register(AccountantRecord)
