from django import forms

from .models import AccountantRecord


class PostForm(forms.Form):
    date = forms.DateField()
    data = forms.DateTimeField()
    group = forms.CharField()
    subgroup = forms.CharField()
    amount = forms.IntegerField()

##FILTER
# class AccountRecordFilter(forms.Form):
#     date_from = forms.DateField()
#     date_to = forms.DateField()










# class PostForm(forms.ModelForm):
#     class Meta:
#         model = AccountantRecord
#         fields = ('title', 'text')
