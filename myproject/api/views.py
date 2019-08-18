from django.shortcuts import render
from .models import AccountantRecord
from .forms import PostForm
from django.shortcuts import redirect
from django.db.models import Sum

def accountant_record(request):
    records = AccountantRecord.objects.all()
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




















# # django views redirect user /"on main page"
# def redirect_views(request):
#     response = redirect('/new/redirect')
#     return response

# # ЗАЧЕМ ЭТО СЮДА ПИСАТЬ ЕСЛИ САЙТ И БЕЗ ЭТОГО ВИДИТ ФОРМУ ??????!!!!!1
# def accountant_record(request):
#     records = PostForm()
#     return render(request, 'list.html', locals())
