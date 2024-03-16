# Generated by Django 5.0.2 on 2024-03-16 23:40

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0007_category_desc'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cate',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='erp.category', verbose_name='Categoría'),
        ),
        migrations.AlterField(
            model_name='product',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='product/%Y/%m/%d', verbose_name='Imagen'),
        ),
        migrations.AlterField(
            model_name='product',
            name='pvp',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=9, verbose_name='Precio de venta'),
        ),
    ]
