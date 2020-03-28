# Generated by Django 3.0.4 on 2020-03-27 21:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('drafts', '0002_auto_20200328_0639'),
    ]

    operations = [
        migrations.AlterField(
            model_name='draft',
            name='person',
            field=models.ForeignKey(blank=True, on_delete=django.db.models.deletion.CASCADE, related_name='person', to='drafts.Person', verbose_name='登録者'),
        ),
    ]
