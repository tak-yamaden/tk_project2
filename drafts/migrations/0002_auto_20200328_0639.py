# Generated by Django 3.0.4 on 2020-03-27 21:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('drafts', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='address',
            field=models.CharField(blank=True, max_length=100, verbose_name='住所'),
        ),
        migrations.AlterField(
            model_name='category',
            name='email',
            field=models.EmailField(blank=True, max_length=50, verbose_name='E-mail'),
        ),
        migrations.AlterField(
            model_name='category',
            name='phone',
            field=models.CharField(blank=True, max_length=30, verbose_name='電話番号'),
        ),
    ]
