# Generated by Django 3.2.15 on 2022-08-14 11:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('TaskApp1', '0003_alter_product_productdocument'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='ProductDocument',
            field=models.FileField(upload_to='pdf/'),
        ),
    ]
