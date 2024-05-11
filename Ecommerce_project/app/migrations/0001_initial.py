# Generated by Django 5.0.4 on 2024-05-03 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Slider',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Image', models.ImageField(upload_to='media/slider_imgs')),
                ('Discount_Deal', models.CharField(choices=[('HOT DEALS', 'HOT DEALS'), ('New Arraivels', 'New Arraivels')], max_length=100)),
                ('SALE', models.IntegerField()),
                ('Brand_Name', models.CharField(max_length=200)),
                ('Discount', models.IntegerField()),
                ('Link', models.CharField(max_length=200)),
            ],
        ),
    ]