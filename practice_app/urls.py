from django.urls import include, path

from . import views

# urlpatterns = [
#     path("", views.index_view, name="index"),
# ]
# urlpatterns = [
#     path("", views.index_form, name="index"),
# ]

urlpatterns = [
    path("insert_practice_page/", views.insert_practice_page, name="insert_practice_page"),
  
    path("insert_practice_data/", views.insert_practice_data, name="insert_practice_data"),
    path("show_practice_page/", views.show_practice_page, name="show_practice_page")
    
]