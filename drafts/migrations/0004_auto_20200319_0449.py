# Generated by Django 3.0.4 on 2020-03-18 19:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('drafts', '0003_auto_20200318_0507'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='draft',
            options={'permissions': [('special_status', 'Can read all books')]},
        ),
    ]
