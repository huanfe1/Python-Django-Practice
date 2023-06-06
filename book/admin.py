from book.models import BookClass, BookInfo, BookISBN, AuthorInfo
from django.contrib import admin


class BookinfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BookClassAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


class BookISBNAdmin(admin.ModelAdmin):
    list_display = ('id', 'isbn')


class AuthorInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(BookClass, BookClassAdmin)
admin.site.register(BookInfo, BookinfoAdmin)
admin.site.register(BookISBN, BookISBNAdmin)
admin.site.register(AuthorInfo, AuthorInfoAdmin)
admin.site.site_header = '管理后台'
admin.site.site_title = '后台管理系统'
