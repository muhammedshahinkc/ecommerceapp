# Generated by Django 4.2.5 on 2023-09-27 07:19

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ecommerceapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='product',
            old_name='avilable',
            new_name='available',
        ),
    ]
