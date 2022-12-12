from django.shortcuts import render, redirect
from .form import ImageForm
from .models import *

def insert_page2(request):
    return render(request, "practice_app2/index3.html")



def insert_data2(request):
    d_name_char = request.POST['char_name']
    d_iteger = request.POST['integer']
    d_slug = request.POST['slug']
    d_text = request.POST['text']
    d_url = request.POST['url']
    d_choice = request.POST['choice']
    

    
    
    # if d_bool == "on":
    #     d_bool_val = True
    # else:
    #     d_bool_val = False

    # new_user = model_practice_app.objects.create(char_name_field=d_char, date_field=d_date, decimal_field=d_decimal, email_field=d_email, boolean_only=d_bool)
    new_user = model_practice2.objects.create(char_name_field2=d_name_char, integer_field=d_iteger, slug_field=d_slug, text_field=d_text, url_field=d_url, choice_field=d_choice)
    print(new_user)
    # return redirect('show_practice_page')

def index4(request):
    if request.method == "POST":
        form=ImageForm(data=request.POST,files=request.FILES)
        if form.is_valid():
            form.save()
            obj=form.instance
            return render(request,"practice_app2/index4.html",{"obj":obj})
    else:
        form=ImageForm()
    img=model_practice4.objects.all()
    print(img)
    return render(request,"practice_app2/index4.html",{"img":img,"form":form})


def index4_1(request):
    return render(request, "practice_app2/index4_1.html")

def insert4_1(request):
    d_char_name = request.POST['char_name']
    # d_image = request.POST['image']
    f_image = request.FILES['image']
    f_file = request.FILES['file']
    # path = 'images/'+ d_image
    # print(d_image)
    print(f_image)
    print(f_file)
    # print(path)
    new_image = model_practice4.objects.create(name_char_field3=d_char_name, image_field=f_image, file_field=f_file)
    new_image.save()
    print(new_image.image_field)
    print(new_image.image_field.url)
    all_data = model_practice4.objects.all()
    print(all_data)
    return render(request, "practice_app2/show4_1.html", {"key1": all_data})
    # return redirect('show_4_1')

def show4_1(request):
    all_data = model_practice4.objects.all()
    print(all_data)
    return render(request, "practice_app2/show4_1.html", {"key1": all_data})


def data(request, id):
    data = model_practice4.objects.get(id=id)
    print(data.file_field)
    print(data.file_field.url)


# def index_s(request):

def show_fkey(request, email):

    s_data = model_student.objects.get(s_email=email)
    print(s_data)
    sd_data = model_sd.objects.get(sd_email=email)
    print(sd_data)
    return render(request, "practice_app2/show_fkey.html", {"key1":s_data, "key2":sd_data})

def show_fkey_all(request):
    ##
    s_data_all = model_student.objects.all()
    # s_data_all_list = list(s_data_all)
    # print(s_data_all_list[1].s_email)
    # sd_data_all = model_sd.objects.all()
    # sd_data_all_list = list(sd_data_all)
    
    # print(s_data_all)
    # print(sd_data_all_list)
    # all_data = []

    ##
    # for i in s_data_all_list:
    #     # print(i['s_email'])
    #     for j in sd_data_all_list:
    #         # print(j['sd_email_id'])
    #         if i["s_email"] == j["sd_email_id"]:
    #             print(i["s_last_name"])
    #             print(j["sd_email_id"])
    #             object = {"s_first_name":i["s_first_name"], "s_first_name":i["s_last_name"], "s_email":i["s_email"], "s_emp_password":i["s_emp_password"], "sd_branch":j["sd_branch"], "sd_age":j["sd_age"], "sd_contact":j["sd_contact"], "sd_city":j["sd_city"]}
    #             all_data.append(object)
                
                
    # print(all_data)
    
    ##
    # all_data = []
    # for i in s_data_all_list:
    #     # print(i.s_email)
    #     # object = {}
    #     for j in sd_data_all_list:
    #         # print(j.sd_email_id)
    #         if i.s_email == j.sd_email_id: 
    #             # print(i.s_last_name)
    #             # print(j.sd_email_id)
    #             print(i.s_email)
    #             object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":j.sd_branch, "sd_age":j.sd_age, "sd_contact":j.sd_contact, "sd_city":j.sd_city} 
    #             all_data.append(object)
    
    # print(all_data)
    # return render(request,"practice_app2/show_fkey_all.html", {"key1":all_data})

    ## handling exception of no entries on second table equivalant to first table
    # all_data_list = []
    # for i in s_data_all:
    #     data = model_sd.objects.filter(sd_email_id = i.s_email).first()
    #     print(data)
    #     # if data == None:
    #     #     print("entry is empty")
    #     if data != None:
    #         object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":data.sd_branch, "sd_age":data.sd_age, "sd_contact":data.sd_contact, "sd_city":data.sd_city}
    #         all_data_list.append(object)



    ##using try and except block exception handle of no equivant entries in second table equivant to first table
    # all_data_list = []
    # for i in s_data_all:
    #     try:
    #         data = model_sd.objects.filter(sd_email_id = i.s_email).first()
    #         # data = model_sd.objects.get(sd_email_id = i.s_email)
    #         print(data)
    #         object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":data.sd_branch, "sd_age":data.sd_age, "sd_contact":data.sd_contact, "sd_city":data.sd_city}
    #         all_data_list.append(object)
    #     except:
    #         object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":"null", "sd_age":"null", "sd_contact":"null", "sd_city":"null"}
    #         all_data_list.append(object)



    ##
    # all_data_list = []
    # for i in s_data_all:
    #     data = model_sd.objects.filter(sd_email_id = i.s_email).first()
    #     print(data)
    #     object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":data.sd_branch, "sd_age":data.sd_age, "sd_contact":data.sd_contact, "sd_city":data.sd_city}
    #     all_data_list.append(object)

        
    #     data = model_sd.objects.filter(sd_email_id = i.s_email)
    #     for i in data:
    #         # print(i)
    #         all_data_list.append(i)
    # print(all_data_list)
        # if data == None:
        #     print("is null")
        #     object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":"null", "sd_age":"null", "sd_contact":"null", "sd_city":"null"}
        #     all_data_list.append(object)
        # # print(data)
        # else:
        #     object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":data.sd_branch, "sd_age":data.sd_age, "sd_contact":data.sd_contact, "sd_city":data.sd_city}
        #     all_data_list.append(object)


        
    # print(all_data_list[0].sd_email_id)
    # print(all_data_list)

    #
    s_data_all = model_student.objects.all()
    all_data_list = []
    for i in s_data_all:
        # data_sd = model_sd.objects.get(sd_email_id = i.s_email)
        data_sd = model_sd.objects.filter(sd_email_id = i.s_email).first()  
        print(data_sd.sd_branch if data_sd != None else "none")                             
        object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":data_sd.sd_branch if data_sd != None else "none", "sd_age":data_sd.sd_age if data_sd != None else "none", "sd_contact":data_sd.sd_contact if data_sd != None else "none", "sd_city":data_sd.sd_city if data_sd != None else "none"}
        all_data_list.append(object)
    print(all_data_list)

    
    return render(request,"practice_app2/show_fkey_all.html", {"key1":all_data_list})
 

def update_onetoone_page(request, email):
    s_data_all = model_student.objects.get(s_email = email)
    sd_data_all = model_sd.objects.get(sd_email=email)
    object = {"id":s_data_all.id, "s_first_name":s_data_all.s_first_name, "s_last_name":s_data_all.s_last_name, "s_email":s_data_all.s_email, "s_emp_password":s_data_all.s_emp_password, "sd_branch":sd_data_all.sd_branch, "sd_age":sd_data_all.sd_age, "sd_contact":sd_data_all.sd_contact, "sd_city":sd_data_all.sd_city}
    print(object)
    print(sd_data_all.sd_age)
    # all_data_list = []
    # for i in s_data_all:
    #     data_sd = model_sd.objects.get(sd_email_id = i.s_email)
    #     print(data_sd)
    #     object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":data_sd.sd_branch, "sd_age":data_sd.sd_age, "sd_contact":data_sd.sd_contact, "sd_city":data_sd.sd_city}
    #     all_data_list.append(object)

    # print(all_data_list)
    return render(request, "practice_app2/update_onetoone.html", {"key1":object})
    # return render(request, "practice_app2/update_onetoone.html")

def update_onetoone(request, email):
    # update_S_first_name = request.POST['f_name']
    # update_S_email = request.POST['email']-
    
    # update_S_last_name = request.POST['l_name']
    # update_S_emp_password = request.POST['psd']
    student_detail = model_student.objects.get(s_email = email)
    # print(student_detail)

    update_Sd_branch = request.POST['branch']
    update_sd_age = request.POST['age']
    update_sd_contact = request.POST['contact']
    update_sd_city= request.POST['city']

    # update_student = model_student.objects.filter(s_email=email).update(s_first_name=update_S_first_name, s_last_name=update_S_last_name, s_email=update_S_email, s_emp_password=update_S_emp_password)
    
    update_sd = model_sd.objects.filter(sd_email=email).update(sd_first_name=student_detail.s_first_name, sd_branch=update_Sd_branch, sd_age=update_sd_age, sd_contact=update_sd_contact, sd_email=student_detail.s_email, sd_city=update_sd_city)
    # update_student.save()
    # update_sd.save() 

    # print(update_student)
    # print(update_sd)
    # update_data = new_model.objects.filter(email = email).update(first_name= update_first_name, last_name = update_last_name, email = update_email, emp_password = update_emp_password)
    
    # print(update_first_name)
    return redirect('show_fkey_all')



    
    #query to save data
    # update_data.save()







def index_s_fkey_page(request):
    return render(request, "practice_app2/index_s_fkey.html")
def index_s_fkey(request):
    s_fname = request.POST["first_name"]
    s_lname = request.POST["last_name"]
    s_email = request.POST["email"]
    s_pass = request.POST["password"]
    new_student = model_student.objects.create(s_first_name=s_fname, s_last_name=s_lname, s_email=s_email, s_emp_password = s_pass)
    print(new_student)
    return redirect('index_sd_fkey_page', s_email)
    # return redirect('index_sd_fkey', s_email)
    # return render(request, "practice_app2/index_sd_fkey.html")


def index_sd_fkey_page(request, email): 
    return render(request, "practice_app2/index_sd_fkey.html", {"key1":email})
    
def index_sd_fkey(request):
    # print(email)
    # return render(request, "practice_app2/index_sd_fkey.html")
    # if(sd_email==email):
    #     get_sd_data = model_sd.objects.get(sd_email=email)
    #     print(get_sd_data.sd_first_name)
    
    # print(email)
    # s_data = model_student.objects.filter(s_email='kailee@gmail.com').first()
    # new_sd = model_sd.objects.create(sd_first_name='ms', sd_branch="tech", sd_age=30, sd_contact="+12123456987", sd_email=s_data, sd_city="goa")
    # print(s_data.s_email)
    sd_fname = request.POST["first_name"]
    sd_branch = request.POST["branch"]
    sd_email_get = request.POST["email"]
    s_data = model_student.objects.get(s_email=sd_email_get)
    
    # sd_email = model_student.objects.filter(s_email='ms.marvel@marvel.com')
    # print("this is email", sd_email[0].s_email)
    sd_age = request.POST["age"]
    sd_contact = request.POST["contact"]
    sd_city = request.POST["city"]

    new_sd = model_sd.objects.create(sd_first_name=sd_fname, sd_branch=sd_branch, sd_age=sd_age, sd_contact=sd_contact, sd_email=s_data, sd_city=sd_city)
    # print(sd_email)
    # new_sd.save()
    return redirect('show_fkey',sd_email_get)

# one_to_many relationship

def index_sc_page(request):
    # (request, email)
    all_data = model_student.objects.all()
    all_email = []
    for i in all_data:
        data = model_sd.objects.filter(sd_email_id=i.s_email).first()
        print(data.sd_email)
        all_email.append(data.sd_email_id)

    print(all_email)
    return render(request,"practice_app2/index_sc.html", {"key1":all_email})


def index_sc(request):
     sc_branch = request.POST["branch"]
     sc_email = request.POST["email"]
     sc_data = model_student.objects.get(s_email=sc_email)

     new_sc = model_sc.objects.create(sc_branch=sc_branch, sc_email=sc_data)
     return redirect('show_fkey', sc_email)

def show_sc(request):
    s_data_all = model_student.objects.all()
    # s_data_all_list = list(s_data_all)
    # print(s_data_all_list[1].s_email)
    # sc_data_all = model_sc.objects.all()
    # sd_data_all_list = list(sd_data_all)

    
    # all_data_list = []
    # for i in s_data_all:
    #     print(i.s_email)
    #     data = model_sc.objects.filter(sc_email_id = i.s_email)
    #     for j in data:
    #         print(j)
    #         if(j.sc_email_id == i.s_email):
    #             print(j)
    #             object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":j.sc_branch, "sc_id":j.id}
    #             all_data_list.append(object)

    ##
    all_data_list = []
    for i in s_data_all:
        # print(i.s_email)
        data = model_sc.objects.filter(sc_email_id = i.s_email)
        # print(data)
        
        print([j for j in data] if len(data) != 0 else "none")

       
        
        # #
        

        # data1 = [i for i in data] if len(data) != 0 else "none"
        # print([data[i] for i in range(len(data1))] if data1 != "none" else "none")
        # c += 1
        


        # if data1 != "none":
        #     print(data1[0].sc_branch)
        # print(data1)
        # # print([i for i in data1] if data1 != "none" else "none")
        # for i in data1:
        #     print(i)

        if len(data) == 0:
            object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":"none", "sc_id":"none"}
            all_data_list.append(object)
        else:
            for j in data:
                print(j)
                if(j.sc_email_id == i.s_email):
                    print(j)
                    object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":j.sc_branch, "sc_id":j.id}
                    all_data_list.append(object)



        

    ##
    # all_data_list = []
    # for i in s_data_all:
    #     print(i)
    #     data = model_sc.objects.filter(sc_email_id = i.s_email)
    #     print([j.sc_branch for j in data] if len(data)!= 0 else "none")
    #     object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":[j.sc_branch for j in data] if len(data)!= 0 else "none", "sc_id":[j.id for j in data] if len(data)!= 0 else "none"}
    #     all_data_list.append(object)
    # print(all_data_list)


    ###
    # all_data_list = []
    # for i in s_data_all:
    #     print(i)
    #     data = model_sc.objects.filter(sc_email_id = i.s_email)
        
        # print(len(data))
        # if len(data) == 0:
        #     print("none")
        # else:
        #     print(data)

        # for j in data:
        #     print(j)
        
        ###
        # print(j.sc_email for j in data if len(data)== 0 else "none")
        # print([i.sc_branch for i in ([j for j in data] if len(data)!= 0 else "none")] if([j for j in data] if len(data)!= 0 else "none") != "none" else "none")
        # print(k.sc_branch for k in [j for j in data] if len(data)!= 0 else "none")
        # print([j.sc_branch for j in data] if len(data)!= 0 else "none")
       
        # itr1 = [j for j in data] if len(data)!= 0 else "none"
        # print(i for i in itr1 if itr1 != "none")
        # if itr1 != "none":
        #     for i in itr1:
        #         print(i)
        # print([j for j in data])

            
        # if (i.sc_email for i in data) == None:
        #     print("no data")

        
        

        ###
        # object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":[j.sc_branch for j in data] if len(data)!= 0 else "none", "sc_id":[j.id for j in data] if len(data)!= 0 else "none"}
        # all_data_list.append(object)

        ##
        # for j in data:
        #     print(j)
            
        #     object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":j.sc_branch if j.sc_email_id == i.s_email else "none", "sc_id":j.id if j.sc_email_id == i.s_email else "none"}
        #     all_data_list.append(object)

                
            
            # print(j.sc_email_id)
    
    ###
    # print(all_data_list)

    #     print(data.sd_email)
    #     object = {"id":i.id, "s_first_name":i.s_first_name, "s_last_name":i.s_last_name, "s_email":i.s_email, "s_emp_password":i.s_emp_password, "sd_branch":data.sd_branch, "sd_age":data.sd_age, "sd_contact":data.sd_contact, "sd_city":data.sd_city}
    #     all_data_list.append(object)
    # all_data_list = []     


    # all_data_list = []
    # for i in s_data_all:
    #     data = model_sc.objects.filter(sc_email_id = i.s_email)
    #     all_data_list.append(data)
    #     print(data)


    # print(all_data_list[3][1])
    # all_objects = []
    # for i in all_data_list:
    #     if len(i) != 0:
    #         for c in i:
    #             data_filter = model_student.objects.filter(s_email=email).first()
                
    #             object = {"id":data_filter.id, "s_first_name":data_filter.s_first_name, "s_last_name":data_filter.s_last_name, "s_email":data_filter.s_email, "s_emp_password":data_filter.s_emp_password, "sd_branch":c}
    #             all_objects.append(object)

    #         print(c)

    # print(all_objects)
 
    # # print(all_data_list[0].sd_email_id)
    # # print(all_data_list)
    return render(request,"practice_app2/show_fkey_all.html", {"key1":all_data_list})

# def update_sc_page(request):
#     return render(request, "practice_app2/show_fkey_all.html")

def update_sc_page(request, email, branch):
    s_data_all = model_student.objects.get(s_email = email)
    sc_data_all = model_sc.objects.get(sc_email_id=email, sc_branch = branch)
    # sc_data_all = model_sc.objects.filter(sc_email_id=email).first()
    print(sc_data_all)
    object = {"id":s_data_all.id, "s_first_name":s_data_all.s_first_name, "s_last_name":s_data_all.s_last_name, "s_email":s_data_all.s_email, "s_emp_password":s_data_all.s_emp_password, "sc_branch":sc_data_all.sc_branch, "sc_id":sc_data_all.id}
    print(object)

    return render(request, "practice_app2/update_sc.html", {"key1": object})

def update_sc(request, email, branch):
    sc_branch = request.POST['branch']
    update_entry = model_sc.objects.filter(sc_email_id = email, sc_branch = branch).update(sc_branch= sc_branch)
    # s_data_all = model_student.objects.get(s_email = email)
    # sc_data_all = model_sc.objects.get(sc_email_id = email, sc_branch = branch)


    # update_data = model_sc.objects.filter(sc_email_id = email)
    

    # for i in update_data:
    #     print(i.id, i.sc_branch)
    #     update_entry = model_sc.objects.filter(id = 2).update(sc_branch= sc_branch)
    #     # print(update_entry.id, update_entry.sc_branch)
        
    return redirect('show_sc')


# many to many

def index_movies_page(request):
    return render(request, "practice_app2/index_movies.html")

def index_movies(request):
    m_name = request.POST["name"]
    new_movie = model_movies.objects.create(m_name=m_name)
    print(new_movie)

def index_characters_page(request):
    all_data = model_movies.objects.all()
    all_movies = []
    for i in all_data:
        print(i.m_name)

        # data = model_characters.objects.filter(id = i.id).first()
        # print(data.c_name)
        all_movies.append(i.m_name)

    print(all_movies)
    return render(request, "practice_app2/index_characters.html", {"key1":all_movies})            

def index_characters(request):
    c_name = request.POST["c_name"]
    movie_name = request.POST["movie"]
    # movie_id = model_movies.objects.filter(m_name=movie_name).first()
    # character_id = model_characters.objects.filter(c_name=c_name).first()
    # print(movie_id.id, movie_id.m_name)
    # print(character_id.id, character_id.c_name)
    new_character = model_characters.objects.create(c_name=c_name)
    print(type(new_character))
    # new_movie_character = character_id.c_movie.add(movie_id.id)
    # print(type(new_movie_character))
    # print(new_character)
    # print(new_movie_character)


    movie = model_movies.objects.filter(m_name = movie_name).first()
    new_concatination = new_character.c_movie.add(movie)


#many_to_many
def index_movies_characters_page(request):
    all_movies = model_movies.objects.all()
    all_movies_set = set(all_movies)
    print(all_movies_set)
    movies = []
    for i in all_movies_set:
        movies.append(i)
    print(movies[1])
    all_characters = model_characters.objects.all()
    all_characters_set = set(all_characters)
    characters = []
    for j in all_characters_set:
        characters.append(j)

    return render(request,"practice_app2/index_movies_characters.html", {"key1": movies, "key2": characters})

def index_movies_characters(request):
    # c_name = model_movies.objects.filter(id=id).first()
    # m_name = model_characters.objects.filter(id=id).first()
    # print(c_name)
    # print(m_name)
    
    # mo1 = model_movies(m_name = "avengers1")
    # mo1.save()
    # mo2 = model_movies(m_name="avengers2")
    # mo2.save()
    # print(mo1.id)
    # print(type(mo2))
    
    # cha1 = model_characters(c_name = "iron man")
    # cha1.save()
    # cha2 = model_characters(c_name="black widow")
    # cha2.save()
    # print(cha1.id)
    # print(type(cha2))

    movies = request.POST["movies"]
    characters=request.POST["characters"]
    print(movies)
    print(characters)
    movies_get=model_movies.objects.filter(m_name=movies).first()
    print(movies_get.id)
    characters_get = model_characters.objects.filter(c_name=characters).first()
    new_movies_characters = characters_get.c_movie.add(movies_get)

    # cha3 = model_characters(c_name = "black panther")
    # cha3.save()
    # mo3 = model_movies(m_name = "avengers3: end game")
    # mo3.save()
    # mo_cha1 = cha3.c_movie.add(mo3)
    # print(mo_cha1)



def show_concatination(request):
    # movies_data = model_movies.objects.all()
    characters_data = model_characters.objects.all()
    movie_character_list = []
    for i in characters_data:
        # print(i.c_name.all())
        print(i.c_name)
        print(i.c_movie.all())
        for j in i.c_movie.all():
            print(j)
            # print(j.m_name)
            # print(j.id)
            movie_character = {"id":j.id, "c_name":i.c_name, "m_name":j.m_name}
            movie_character_list.append(movie_character)
    # print(characters_data[1].c_movie.all().first().id)
    print(movie_character_list)
    return render(request, "practice_app2/show_concationation.html", {"key1": movie_character_list})

def update_concatination_page(request, movie, character):
    # movie_data = model_movies.objects.filter(m_name = movie).first()
    # character_data = model_characters.objects.filter(c_name = character).first()
    return render(request, "practice_app2/update_concaticnation.html", {"key1" : movie, "key2" : character})


def update_concatination(request, character):
    # movie_data_get = request.POST['movie']
    character_data_get = request.POST['character']

    # movie_data = model_movies.objects.filter(m_name = movie)
    character_data = model_characters.objects.filter(c_name = character).update(c_name = character_data_get)

    return redirect('show_concatination')
    











