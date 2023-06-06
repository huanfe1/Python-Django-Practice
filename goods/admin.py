import xadmin
from .models import GoodsInfo
from xadmin import views


class BaseSetting(object):
    enable_themes = True
    use_bootswatch = True


class GoodsInfoAdmin(object):
    list_display = ('id', 'name', 'price', 'weight', 'isnew')
    list_editable = ('price', 'weight')
    list_filter = ['name', 'price']
    search_fields = ('name',)


class GlobalSettings(object):
    site_title = '商品后台管理系统'
    site_footer = '版权归属@东营科技有限公司'


xadmin.site.register(GoodsInfo, GoodsInfoAdmin)
xadmin.site.register(views.BaseAdminView, BaseSetting)
xadmin.site.register(views.CommAdminView, GlobalSettings)
