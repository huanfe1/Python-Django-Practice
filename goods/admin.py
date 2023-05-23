from django.contrib import admin
from goods.models import GoodsInfo
from django.utils.html import mark_safe


class GoodsInfoAdmin(admin.ModelAdmin):
    def buttons(self, obj):
        button_html = '''
        <a class="changelink" href="http://127.0.0.1:8000/admin/goods/goodsinfo/%s/change/">编辑</a>
        ''' % obj.id
        return mark_safe(button_html)

    buttons.short_description = '操作'

    def good_img(self, obj):
        img_html = '''
        <img src="/%s" width="40px" height="40px">
        ''' % obj.image
        return mark_safe(img_html)

    good_img.short_description = '商品图片'
    list_display = ('id', 'name', 'price', 'isnew', 'buttons', 'good_img')
    list_editable = ('price', 'isnew')
    search_fields = ('name',)


admin.site.register(GoodsInfo, GoodsInfoAdmin)
admin.site.site_header = '商品信息管理后台'
admin.site.site_title = '后台管理系统'
