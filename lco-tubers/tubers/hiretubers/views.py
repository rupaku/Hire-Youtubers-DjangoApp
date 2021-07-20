from django.shortcuts import render,redirect
from .models import HireTuber
# Create your views here.

def hiretuber(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        tuber_id = request.POST['tuber_id']
        tuber_name = request.POST['tuber_name']
        city = request.POST['city']
        phone = request.POST['phone']
        state = request.POST['state']
        message = request.POST['message']
        user_id = request.POST['user_id']
        created_date = request.POST['created_date']

        # TODO: Do all sanitization
        hiretuber = HireTuber(first_name=first_name,
                              last_name=last_name,
                              tuber_id=tuber_id,
                              tuber_name=tuber_name,
                              city=city,
                              phone=phone,
                              state=state,
                              message=message,
                              user_id=user_id,
                              created_date=created_date)

        hiretuber.save()

        message.success(request,'Thanks for reaching out!')
        return redirect('youtubers')