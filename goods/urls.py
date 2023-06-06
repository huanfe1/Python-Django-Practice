from django.urls import path, re_path

from . import views

app_name = 'goods'
urlpatterns = [
    path('goodslist/', views.GoodsListView.as_view()),
    re_path(r'gooddetail/(?P<goods_id>\d+)/$', views.detailView.as_view(), name='gooddetail')
]
