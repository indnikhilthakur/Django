from django.urls import include, path

from . import views



urlpatterns = [
    path("insert_page2/", views.insert_page2, name="insert_page2"),
    path("insert_data2/", views.insert_data2, name="insert_data2"),
  
    path("index4/", views.index4, name="index4"),
    path("index4_1/", views.index4_1, name="index4_1"),
    path("insert4_1/", views.insert4_1, name="insert4_1"),
    path("show4_1/", views.show4_1, name="show4_1"),
    path("data/<int:id>", views.data, name="data"),
    path("show_fkey/<str:email>", views.show_fkey, name="show_fkey"),
    path("index_s_fkey_page/", views.index_s_fkey_page, name="index_s_fkey_page"),
    path("index_s_fkey/", views.index_s_fkey, name="index_s_fkey"),
    path("index_sd_fkey/", views.index_sd_fkey, name="index_sd_fkey"),
    path("index_sd_fkey_page/<str:email>", views.index_sd_fkey_page, name="index_sd_fkey_page"),
    path("show_fkey_all/", views.show_fkey_all, name="show_fkey_all"),
    path("index_sc_page/", views.index_sc_page, name="index_sc_page"),
    path("index_sc/", views.index_sc, name="index_sc"),
    path("show_sc/", views.show_sc, name="show_sc"),
    path("index_movies_page/", views.index_movies_page, name="index_movies_page"),
    path("index_movies/", views.index_movies, name="index_movies"),
    path("index_characters_page/", views.index_characters_page, name="index_characters_page"),
    path("index_characters/", views.index_characters, name="index_characters"),
    path("index_movies_characters/<int:id>", views.index_movies_characters, name="index_movies_characters"),
    path("index_movies_characters_page/", views.index_movies_characters_page, name="index_movies_characters_page"),
    path("index_movies_characters/", views.index_movies_characters, name="index_movies_characters"),
    path("show_concatination/", views.show_concatination, name="show_concatination"),
    path("update_onetoone_page/<str:email>", views.update_onetoone_page, name="update_onetoone_page"),
    path("update_onetoone/<str:email>", views.update_onetoone, name="update_onetoone"),
    path("update_sc_page/<str:email>/<str:branch>", views.update_sc_page, name="update_sc_page"),
    path("update_sc/<str:email>/<str:branch>", views.update_sc, name="update_sc"),
    path("update_concatination_page/<str:movie>/<str:character>", views.update_concatination_page, name="update_concatination_page"),
    path("update_concatination/<str:character>", views.update_concatination, name="update_concatination"),
    # path("index_sd_fkey1", views.index_sd_fkey1, name="index_sd_fkey1"),
    # path("insert_practice_data/", views.insert_practice_data, name="insert_practice_data"),
    # path("show_practice_page/", views.show_practice_page, name="show_practice_page")
    
]