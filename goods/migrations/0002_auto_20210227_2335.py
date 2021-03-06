# Generated by Django 2.0.6 on 2021-02-27 15:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goods',
            name='alias',
            field=models.CharField(max_length=50, null=True, verbose_name='别名'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='counter',
            field=models.IntegerField(null=True, verbose_name='库存'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='price',
            field=models.DecimalField(decimal_places=2, max_digits=9, null=True, verbose_name='价格'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='sale_counter',
            field=models.IntegerField(null=True, verbose_name='累计销量'),
        ),
        migrations.AlterField(
            model_name='goods',
            name='units',
            field=models.IntegerField(null=True, verbose_name='单位'),
        ),
    ]
