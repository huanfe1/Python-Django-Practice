from DjangoUeditor.models import UEditorField
from django.db import models


class GoodsInfo(models.Model):
    name = models.CharField(max_length=30, verbose_name='商品名称')
    price = models.FloatField(verbose_name='商品价格', default=20.0)
    weight = models.IntegerField(verbose_name='商品重量', default=500)
    image = models.ImageField(upload_to='upload/%Y/%m', verbose_name='商品图片', default='upload/default.jpg')
    isnew = models.BooleanField(verbose_name='是否新品', default=False)
    # details = models.TextField(verbose_name='商品详情', default='')
    details = UEditorField(verbose_name='商品详情', default='', toolbars='full')

    def __str__(self):
        return self.name
