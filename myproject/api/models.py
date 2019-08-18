import datetime
from django.db import models

class AccountantRecord(models.Model):
    date = models.DateField(null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    group = models.TextField(max_length=250)
    subgroup = models.TextField(max_length=250)
    amount = models.IntegerField()

    class Meta:
        db_table = "Accountant_record"


