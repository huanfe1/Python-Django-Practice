from django.shortcuts import render
from django.views.generic.list import ListView
from goods.models import GoodsInfo
from django.views.generic.detail import DetailView


class GoodsListView(ListView):
    model = GoodsInfo
    template_name = 'goodslist.html'
    context_object_name = 'goods'


class detailView(DetailView):
    def get(self, request, goods_id):
        goods = GoodsInfo.objects.get(id=int(goods_id))
        return render(request, 'gooddeail.html', {'goods': goods})
