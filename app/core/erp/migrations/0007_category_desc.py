# Generated by Django 5.0.2 on 2024-03-05 03:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('erp', '0006_client_alter_category_name_product_sale_detsale_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='desc',
            field=models.CharField(blank=True, max_length=500, null=True, verbose_name='Descripcion'),
        ),
    ]
