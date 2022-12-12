from django.shortcuts import render, redirect
from .models import *

# Create your views here.

def insert_practice_page(request):
    return render(request, "practice_app/index.html")

def insert_practice_data(request):
    d_char = request.POST['char_name']
    d_date = request.POST['date']
    d_decimal = request.POST['decimal']
    d_email = request.POST['email']
    d_bool = request.POST['bool_only']
    # d_choice = request.POST['city']
    print(d_bool)

    
    
    # if d_bool == "on":
    #     d_bool_val = True
    # else:
    #     d_bool_val = False

    new_user = model_practice_app.objects.create(char_name_field=d_char, date_field=d_date, decimal_field=d_decimal, email_field=d_email, boolean_only=d_bool)
    print(new_user)
    return redirect('show_practice_page')


# def insert_data(request):
#     #comes data from form
#     f_name = request.POST["f_name"]
#     l_name = request.POST["l_name"]
#     email = request.POST["email"]
#     psd = request.POST["psd"]

#     print(type(email))
#     #creating object into model class
#     # insert data into table                
#     new_user = new_model.objects.create(first_name=f_name, last_name=l_name, email=email, emp_password=psd)
#     print(new_user)
    
#     # after insert render into show.html
#     # return render(request, "new_app/show.html")
    
#     # after render insert show_page view
#     return redirect('show_page')

def show_practice_page(request):
    # select* from table
    # all_data = new_model.objects.all().order_by('last_name').values()
    all_data = model_practice_app.objects.all()
    # all_data_filter = new_model.objects.filter(first_name='steve', last_name='rogers').values()
    # all_data_filter = new_model.objects.filter().last()
    # all_data_filter = new_model.objects.filter().first()
    # all_data_filter = new_model.objects.values_list('first_name')


    # all_data = new_model.objects.all().values()
    # z = all_data.__len__()
    # c = len(all_data) -1
    # z = all_data[c]
    # print(z)
    
    # queryset_list = list(all_data)
    # print(queryset_list[1].email)
    
    # return render(request, "new_app/show_page.html", {'key1': all_data, "key2": z, "key_2": queryset_list})
    return render(request, "practice_app/show_page.html", {'key1': all_data})



     
def insert_practice_page2(request):
    return render(request, "practice_app/index2.html")
