# Generated by Django 3.2 on 2023-05-02 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0002_user_is_staff'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='item_image',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
