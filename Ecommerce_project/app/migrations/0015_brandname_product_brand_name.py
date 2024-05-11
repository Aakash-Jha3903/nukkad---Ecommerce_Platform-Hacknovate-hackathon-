# Generated by Django 5.0.4 on 2024-05-10 18:20

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0014_product_color'),
    ]

    operations = [
        migrations.CreateModel(
            name='BrandName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('brandname', models.CharField(max_length=100)),
            ],
        ),
        migrations.AddField(
            model_name='product',
            name='brand_name',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='app.brandname'),
        ),
    ]