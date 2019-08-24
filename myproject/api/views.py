
from datetime import datetime
from django.shortcuts import render
from .models import AccountantRecord
from .forms import PostForm
from django.shortcuts import redirect
from django.db.models import Sum

def accountant_record(request):
    order = request.GET.get('order', '-date')

    start_date = datetime.now().replace(day=1).strftime('%Y-%m-%d')
    if 'from' in request.GET:
        start_date = request.GET['from']
        start_date = datetime.strptime(start_date, '%Y-%m-%d')


    end_date = datetime.now().strftime('%Y-%m-%d')
    if 'to' in request.GET and request.GET['to'] != "":
        end_date = request.GET['to']
        end_date = datetime.strptime(end_date, '%Y-%m-%d')

    records = AccountantRecord.objects.filter(date__range=(start_date, end_date)).order_by(order)

    total_amount = AccountantRecord.objects.aggregate(Total_amount=Sum('amount'))

    return render(request, 'list.html', locals())

# С request вытянуть параметры формы и создать "accountant_record_new"

# ТУТ ВОПРОС ПО ""rec"""
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


#FILTER
# def account_record_filter(request):
#     arf = accountant_record_new.objects.order_by('group')
#     return redirect("/")

#SORTED Это для того чтобы изначально отсортировать всю таблицу по дате записи,а похже сделать для периода и группы затрат



#### Фильтрация за текущий месяц вроде бы
#MyModel.objects.filter(My_DATE_FIELD__date=timezone.now()












# # django views redirect user /"on main page"
# def redirect_views(request):
#     response = redirect('/new/redirect')
#     return response

# # ЗАЧЕМ ЭТО СЮДА ПИСАТЬ ЕСЛИ САЙТ И БЕЗ ЭТОГО ВИДИТ ФОРМУ ??????!!!!!1
# def accountant_record(request):
#     records = PostForm()
#     return render(request, 'list.html', locals())
