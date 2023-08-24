from django.db import models
from django.utils.html import format_html
from django.contrib import admin

class Advertisement(models.Model):
    title = models.CharField('заголовок', max_length=128)
    description = models.TextField('описание')
    price = models.DecimalField('цена', max_digits=10, decimal_places=2)
    auction = models.BooleanField('торг', help_text='Отметьте, если торг уместен')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    @admin.display(description='дата создания')
    def created_date(self):
        from django.utils import timezone
        if self.created_at.date() == timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html(f'<span style="color: green"; font-weight: bold;">Сегодня в {created_time}</span>')
        return self.created_at.strftime('%d.%m.%Y в %H:%M:%S ')

    @admin.display(description='дата обновления')
    def updated_date(self):
        from django.utils import timezone
        if self.updated_at.date() == timezone.now().date():
            updated_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(f'<span style="color: red"; font-weight: bold;">Сегодня в {updated_time}</span>')
        return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S ')

    def __str__(self):
        return f'Advertisement(id=-{self.id}, title={self.title}, price={self.price} '
    class Meta:
        db_table = 'app_adv_advertisement'