# Generated by Django 5.0.4 on 2024-05-03 21:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0004_maincategory_category_subcategory'),
    ]

    operations = [
        migrations.RenameField(
            model_name='subcategory',
            old_name='main_category',
            new_name='category',
        ),
    ]
