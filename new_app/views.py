from django.shortcuts import render, redirect
from .models import *
from django.http import Http404
from django.shortcuts import render, get_object_or_404

# Create your views here.
# def index_view(request):
#     return render(request, "new_app/index.html")

# def index_form(request):
#     return render(request, "new_app/index.html")
def test_model_practice(request):
    return render(request, "new_app/test_model_practice.html")


def test_practice(request):
    #comes data from form
    

    field1 = request.POST["bool_checkbox"]
    field2 = request.POST["bool_checkbox_multi"]
    field3 = request.POST["char"]
    field4 = request.POST["date"]
    field5 = request.POST["decimal"]
    field6 = request.POST["email"]
    field7 = request.POST["file"]
    field8 = request.POST["image"]
    field9 = request.POST["integer"]
    field10 = request.POST["slug"]
    field11 = request.POST["text"]
    field12 = request.POST["url"]
    field13 = request.POST["uuid1"]
    field14 = request.POST["uuid2"]
    field15 = request.POST["update_date"]
    field16 = request.POST["created_date"]
    field17 = request.POST["date_time"]
    field18 = request.POST["choices"]


    
    #creating object into model class
    # insert data into table                
    new_user = new_model.objects.create(boolean_only=field1, boolean_multi=field2, char_field=field3, date_field=field4, decimal_field=field5, email_field=field6, file_field=field7, image_field=field8, integer_field=field9, slug_field=field10, text_field=field11, url_field=field12, uuid1=field13, uuid2=field14, updated_date=field15, created_date=field16, date_and_time=field17, choice_field=field18)
    # new_user = new_model.objects.create(char_field = field3)
    print(new_user)

    
    # after insert render into show.html
    # return render(request, "new_app/show.html")
    
    # after render insert show_page view
    # return redirect('show_page')

def insert_page(request):
    return render(request, "new_app/index.html")
# def id_test_page(request, id):
#     print(id)
#     return render(request, "new_app/id_test_page.html")

def id_test(request, id):
    all_data = new_model.objects.all()
    queryset_list = list(all_data)
    # all_data = new_model.objects.values("id", "first_name")
    # all_data = new_model.objects.values()
    print(all_data)
    print(queryset_list[0].id)

    flag = 0
    for i in all_data:
        print(i.id)
        if id==i.id:
            flag += 1
        #     print("id existed")

        # else:
        #     print("id dosent exist")

    # filter_entry = []
    if flag == 1:
        filter_entry= new_model.objects.get(id=id)
        # filter_data = list(filter_entry)
        print("id existed")
        # print(filter_data)
        print(filter_entry)
    else:
        print("id dosent exist")

    print(filter_entry)

    # return redirect('show_page', {"key_2":fiter_entry})
    return render(request, "new_app/id_test_page.html", {'key_2': filter_entry})

def email_validation(request, id, email):
   
    # method #1
    # get_data = new_model.objects.get(email=email)
    # # get_data = new_model.objects.filter(email=email).first
    # print(get_data)

    # if get_data.email:

    #     print("email id existed")
    # else:
    #     print("not exist")
    #     # redirect('index')


    # method #2
    # get_data = new_model.objects.filter(id=id, email=email).first()
    # print(get_data)

    # if get_data == None:
    #     print("not exist")

    # else:
    #     print("email id existed")

    # method 4 for seperate id and email
    get_data_id = new_model.objects.filter(id=id).first()
    get_data_email = new_model.objects.filter(email=email).first()
    print(get_data_email)
    print(get_data_id)

    if get_data_id == None and get_data_email == None: 
        print("id and email does not exist")
        # return redirect('insert_page')
        return redirect('update_page_email', email)

    elif get_data_id == None and get_data_email != None:
        print("id does not exist")
        print("email is existed")
        # update_data = new_model.objects.filter(email=email).update(id=id)
        # return redirect('test_show_page')
        
    elif get_data_id != None and get_data_email == None:
        print("id is existed")
        print("email does not exist")
        # update_data = new_model.objects.filter(id = id).update(email=email)
        # return redirect('test_show_page')
    else:
        print("id and email existed")

        # return render(request, "new_app/update_page.html", {'key_2': get_data_email})
        return redirect('update_page', email)
        # return redirect('update_entry', id)


    
    # method #3
    # try:
    #     get_data = new_model.objects.get(id=id, email=email)
    #     print("email already exist")
    # except new_model.DoesNotExist:
    #     print("does not exist")
    #     # raise insert_page
        
    #     raise Http404

    # method #5
    # try:
    #     get_data = new_model.objects.get(id=id, email=email)
    #     print("email already exist")
    # except new_model.DoesNotExist:
    #     print("does not exist")
    #     # raise insert_page
        
    #     raise Http404
       
    # # return redirect('id_test_page')
    # return render(request, "new_app/id_test_page.html", {'key_2': get_data})    

def update_page_email(request, email):
    # get_data = new_model.objects.get(email=email)
    # print(get_data.email)

    get_email = email
    print(get_email)
    
    # return render(request, "new_app/update_page_email", {'key3':get_data})
    return render(request, "new_app/insert_page_email.html", {'key_2':get_email})

def validation(request):
    f_name = request.POST["f_name"]
    l_name = request.POST["l_name"]
    email = request.POST["email"]
    psd = request.POST["psd"]
    print(email)
    all_data = new_model.objects.all()
    queryset_list = list(all_data)
    # c = len(queryset_list) -1
    print(queryset_list)
    flag = 0
    for i in queryset_list:
        print(i.email)
        if email == i.email:
            flag += 1
        #     # if queryset_list[c].email == i.email:
        #     # print("given email is already existed")
            
        # else:
        #     if queryset_list[c].email == i.email:
        #         print("entered")
    if flag == 1:
        print("given email is already existed")
    else:
        print("entered")
        new_user = new_model.objects.create(first_name=f_name, last_name=l_name, email=email, emp_password=psd)

        return redirect('test_show_page')

    

def insert_data(request):
    #comes data from form
    f_name = request.POST["f_name"]
    l_name = request.POST["l_name"]
    email = request.POST["email"]
    psd = request.POST["psd"]

    print(type(email))
    #creating object into model class
    # insert data into table                
    new_user = new_model.objects.create(first_name=f_name, last_name=l_name, email=email, emp_password=psd)
    print(new_user)
    
    # after insert render into show.html
    # return render(request, "new_app/show.html")
    
    # after render insert show_page view
    return redirect('show_page')
#show page view
def show_page(request):
    # select* from table
    # all_data = new_model.objects.all().order_by('last_name').values()
    all_data = new_model.objects.all()
    # all_data_filter = new_model.objects.filter(first_name='steve', last_name='rogers').values()
    # all_data_filter = new_model.objects.filter().last()
    # all_data_filter = new_model.objects.filter().first()
    # all_data_filter = new_model.objects.values_list('first_name')


    # all_data = new_model.objects.all().values()
    # z = all_data.__len__()
    c = len(all_data) -1
    z = all_data[c]
    print(z)
    
    queryset_list = list(all_data)
    print(queryset_list[1].email)
    
    return render(request, "new_app/show.html", {'key1': all_data, "key2": z, "key_2": queryset_list})
    # return render(request, "new_app/show.html", {'key1': all_data, "key2": z, "key8":all_data_filter})

def test_show_page(request):
    # fetch_data = new_model.objects.all().values_list()
    fetch_data = new_model.objects.all()
    # fetch_data = new_model.objects.all().order_by('last_name').values()
    # fetch_data = new_model.objects.filter(first_name='steve', last_name='rogers').values()
    # fetch_data1 = new_model.objects.filter(first_name='steve')
    # print(fetch_data1)
    
    

    z=len(fetch_data) -1

    # print(type(len(z)))
    # print(fetch_data[0][0])
    # n = z-1
    # all_data = new_model.objects.filter(id=n)
    
    queryset_list = list(fetch_data)
    print(queryset_list[0].email)
    

    return render(request, "new_app/test_show_page.html", {'key9': fetch_data, "key12":z, "key_12": queryset_list})

def single_column_show_page(request):
    all_data_single_column = new_model.objects.all()
    queryset_list = list(all_data_single_column)
     
    # # list = []
    for i in queryset_list:
        print(i.last_name)
        # list.append(i.last_name)

    print(list)    
    last_name_column = queryset_list[0].last_name
    # print(queryset_list[0].last_name)

    # return render(request, "new_app/single_column_show_page.html", {"key_1":all_data_single_column, "key_3":last_name_column})
    # return render(request, "new_app/single_column_show_page.html", {"key_1":all_data_single_column})
    return render(request, "new_app/single_column_show_page.html", {"key_1":queryset_list})

def update_entry(request, id):
    l_name = "chang"
    update_data = new_model.objects.filter(id = id).update(first_name= "shang", last_name = l_name, email = "shang_chi5@gmail.com", emp_password = "shang")
    return redirect('test_show_page')





def update_page(request, email):
    #fetching data of perticuler id
    get_data = new_model.objects.get(email=email)
    # get_data_email = new_model.objects.get(email=email)
    # print(get_data_email)
    # get_data_filter = new_model.objects.filter()
    print(get_data.email)
    return render(request, "new_app/update.html", {'key3': get_data})


#updating data entry from table in update_page     


def update_data(request, email):
    # update_data = new_model.objects.get(email=email)
    # update_data.first_name = request.POST['f_name']
    # update_data.last_name = request.POST['l_name']
    # update_data.email = request.POST['email']
    # update_data.emp_password = request.POST['psd']
    
    update_first_name = request.POST['f_name']
    update_last_name = request.POST['l_name']
    update_email = request.POST['email']
    update_emp_password = request.POST['psd']

    update_data = new_model.objects.filter(email = email).update(first_name= update_first_name, last_name = update_last_name, email = update_email, emp_password = update_emp_password)
    
    print(update_first_name)

    
    #query to save data
    update_data.save()
    # render to show page
    # return redirect('show_page')

#create function to delete data
def delete_data(request, pk):
    del_data =new_model.objects.get(id=pk)
    # del_data = new_model.objects.filter(email='ms.marvel1@marvel.com')
    # query to delete data
    del_data.delete()
    return redirect('test_show_page')