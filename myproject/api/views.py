
from datetime import datetime
from django.shortcuts import render
from .models import AccountantRecord
from .forms import PostForm
from django.shortcuts import redirect
from django.db.models import Sum

def accountant_record(request):
    order = request.GET.get('order', '-date')
    start_date = datetime.now().replace(day=1)
    if 'from' in request.GET and request.GET['from'] != "":
        start_date = request.GET['from']
        start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.now().strftime('%Y-%m-%d')
    if 'to' in request.GET and request.GET['to'] != "":
        end_date = request.GET['to']
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

    records = AccountantRecord.objects.filter(date__range=(start_date, end_date)).order_by(order)
    filter_group = ""
    if 'filter_group' in request.GET and request.GET['filter_group'] != "":
        filter_group = request.GET["filter_group"]
        records = records.filter(group=filter_group)

    total_amount = AccountantRecord.objects.aggregate(Total_amount=Sum('amount'))

    groups = AccountantRecord.objects.values_list('group', flat=True).distinct().order_by('group')
    subgroups = AccountantRecord.objects.values_list('subgroup', flat=True).distinct().order_by('subgroup')

    return render(request, 'list.html', locals())




def accountant_record_new(request):
    rec = AccountantRecord.objects.create(date=request.POST['date'],
                                          group=request.POST['group'],
                                          subgroup=request.POST['subgroup'],
                                          amount=request.POST['amount'])
    response = redirect('/')
    return response

def account_record_delete(request, id):
    dele = AccountantRecord.objects.get(id=id).delete()
    return redirect("/")


