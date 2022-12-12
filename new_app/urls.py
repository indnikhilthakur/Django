
from django.urls import include, path

from . import views

# urlpatterns = [
#     path("", views.index_view, name="index"),
# ]
# urlpatterns = [
#     path("", views.index_form, name="index"),
# ]

urlpatterns = [
    path("", views.insert_page, name="insert_page"),
    path("test_model_practice/", views.test_model_practice, name="test_model_practice"),
    path("test_practice/", views.test_practice, name="test_practice"),
    path("index/", views.insert_data, name="index"),
    path("show_page/", views.show_page, name="show_page"),
    path("update_page/<int:pk>", views.update_page, name="update_page"),
    path("update_page/<str:email>", views.update_page, name="update_page"),
    # path("update_page/<int:pk>/, update_page/<str:email>/", views.update_page, name="update_page"),
    # path("update_page/<str:email>", views.update_page, name="update_page"),
    # path("update_data/<int:pk>", views.update_data, name="update_data"),
    path("update_data/<str:email>", views.update_data, name="update_data"),
    # path("update_data/<str:email_id>", views.update_data, name="update_data"),
    path("update_entry/<int:id>", views.update_entry, name="update_entry"),
    path("test_show_page/", views.test_show_page, name="test_show_page"),
    path("single_column_show_page/", views.single_column_show_page, name="single_column_show_page"),
    path("validation/", views.validation, name="validation"),
    path("id_test/<int:id>", views.id_test, name="id_test"),
    # path("id_test_page/<int:id>", views.id_test_page, name="id_test_page"),
    path("email_validation/<int:id>/<str:email>", views.email_validation, name="email_validation"),
    path("update_page_email/<str:email>", views.update_page_email, name="update_page_email"),
    path("delete_data/<int:pk>", views.delete_data, name="delete_data"),
]