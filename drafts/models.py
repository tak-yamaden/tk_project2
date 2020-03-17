import uuid
from django.db import models
from django.contrib.auth import get_user_model
from django.utils import timezone
from django.urls import reverse

class Category(models.Model):
    company = models.CharField('会社名', max_length=30)
    phone = models.CharField('電話番号', max_length=30)
    email = models.EmailField('E-mail', max_length=50)

    def __str__(self):
        return self.company


class Person(models.Model):
    first_name = models.CharField('名', max_length=20)
    last_name = models.CharField('姓', max_length=20)
    email = models.EmailField('E-mail', max_length=50)
    hire_date = models.DateTimeField('入社日', default=timezone.now, blank=True)
    is_active = models.BooleanField(default=False)

    def __str__(self):
        return '{} {}'.format(self.last_name, self.first_name)

class Status(models.Model):
    STATUS =(
        ('A', '新規登録'),
        ('B', '設計変更'),
        ('C', '図面廃止'),
    )

class Draft(models.Model):
    id = models.UUIDField(
        primary_key=True,
        default= uuid.uuid4,
        editable=False,
    )
    company_name = models.CharField('会社名', max_length=50)
    y_number = models.CharField('Y品番', max_length=20, blank=True)
    number = models.CharField('番号', max_length=20, blank=True)
    product_name = models.CharField('製品名', max_length=50)
    person = models.ForeignKey(Person, verbose_name='登録者', on_delete=models.CASCADE)
    status = models.CharField('状況', max_length=1, choices=Status.STATUS)
    created_at = models.DateTimeField('日付', default=timezone.now)
    category = models.ForeignKey(Category, verbose_name='カテゴリー', on_delete=models.CASCADE, blank=True, default='')
    cover = models.ImageField('図面', upload_to='covers/', blank=True)
    is_active = models.BooleanField(default=False)

    class Meta:
        permissions = [
            ('special_status', 'Can read all books'),
        ]

    def __str__(self):
        return self.product_name

    def get_absolute_url(self):
        return reverse('draft_detail', args=[str(self.id)])

