from django.shortcuts import render
from book.models import BookClass, BookInfo, AuthorInfo
from django.http import HttpResponse
from django.views.generic.list import ListView


class AuthorListView(ListView):
    model = AuthorInfo
    template_name = "list.html"
    context_object_name = "my_author"


def add_book_class(request):
    # obj = BookClass(name='文学类')
    # obj.save(obj)
    # return HttpResponse("添加成功")
    BookInfo.objects.create_bookinfo('畅销书籍')
    return HttpResponse("添加成功")


def del_book_class(request):
    class_name = BookClass.objects.filter(name='文学类')
    if class_name:
        class_name.delete()
        return HttpResponse("删除成功")
    else:
        return HttpResponse("未找到数据")


def update_book_class(request):
    class_name = BookClass.objects.filter(name='文学类')
    if class_name:
        class_name.update(name='小说类')
        return HttpResponse("修改成功")
    else:
        return HttpResponse("未找到数据")


def get_book_class(request):
    book_class_list = BookClass.objects.all()
    if book_class_list:
        book_class_names = [book_class.name for book_class in book_class_list]
        return HttpResponse("查询到的图书分类有：" + ",".join(book_class_names))
    else:
        return HttpResponse("未找到数据")


def page_not_found(request, exception):
    return render(request, '404.html')
