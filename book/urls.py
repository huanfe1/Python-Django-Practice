from django.urls import path
from . import views

app_name = 'book'
urlpatterns = [
    path('addbookclass/', views.add_book_class),
    path('delbookclass/', views.del_book_class),
    path('updatebookclass/', views.update_book_class),
    path('getbookclass/', views.get_book_class),
    path('authorlist/', views.AuthorListView.as_view()),
]

handler404 = views.page_not_found
