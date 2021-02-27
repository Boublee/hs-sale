from django.db import models


# Create your models here.
class Goods(models.Model):
    code = models.CharField(verbose_name='商品代码', max_length=10)
    title = models.CharField(verbose_name='名称', max_length=50)
    alias = models.CharField(verbose_name='别名', max_length=50, null=True)
    price = models.DecimalField(verbose_name='价格', max_digits=9, decimal_places=2, null=True)
    units = models.IntegerField(verbose_name='单位', null=True)
    counter = models.IntegerField(verbose_name='数量', null=True, default=0)
    sale_counter = models.IntegerField(verbose_name='累计销量', null=True)
