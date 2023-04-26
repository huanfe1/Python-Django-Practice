from django.contrib import admin
from goods.models import GoodsInfo


# Register your models here.
class GoodsInfoAdmin(admin.ModelAdmin):
    list_display = ('id', 'name')


admin.site.register(GoodsInfo, GoodsInfoAdmin)
