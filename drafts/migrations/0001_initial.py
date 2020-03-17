# Generated by Django 3.0.4 on 2020-03-17 19:57

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=30, verbose_name='会社名')),
                ('phone', models.CharField(max_length=30, verbose_name='電話番号')),
                ('email', models.EmailField(max_length=50, verbose_name='E-mail')),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('first_name', models.CharField(max_length=20, verbose_name='名')),
                ('last_name', models.CharField(max_length=20, verbose_name='姓')),
                ('email', models.EmailField(max_length=50, verbose_name='E-mail')),
                ('hire_date', models.DateTimeField(blank=True, default=django.utils.timezone.now, verbose_name='入社日')),
                ('is_active', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Draft',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('company_name', models.CharField(max_length=50, verbose_name='会社名')),
                ('y_number', models.CharField(blank=True, max_length=20, verbose_name='Y品番')),
                ('number', models.CharField(blank=True, max_length=20, verbose_name='番号')),
                ('product_name', models.CharField(max_length=50, verbose_name='製品名')),
                ('status', models.CharField(choices=[('A', '新規登録'), ('B', '設計変更'), ('C', '図面廃止')], max_length=1, verbose_name='状況')),
                ('created_at', models.DateTimeField(default=django.utils.timezone.now, verbose_name='日付')),
                ('cover', models.ImageField(blank=True, upload_to='covers/', verbose_name='図面')),
                ('is_active', models.BooleanField(default=False)),
                ('category', models.ForeignKey(blank=True, default='', on_delete=django.db.models.deletion.CASCADE, to='drafts.Category', verbose_name='カテゴリー')),
                ('person', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='drafts.Person', verbose_name='登録者')),
            ],
            options={
                'permissions': [('special_status', 'Can read all books')],
            },
        ),
    ]
