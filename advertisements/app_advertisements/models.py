from django.db import models
from django.contrib import admin
from django.utils import timezone
from django.contrib.auth import get_user_model
from django.utils.html import format_html

# Create your models here.

User = get_user_model()
class Advertisement(models.Model):
    title = models.CharField('Заголовок',max_length=128)
    description = models.TextField('Описание')
    price = models.DecimalField('Цена',max_digits=10,decimal_places=2)
    auction = models.BooleanField('Торг', help_text='Укажите, уместен ли торг')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    user = models.ForeignKey(User, verbose_name='Пользователь', on_delete=models.CASCADE)
    image = models.ImageField( 'Изображение', upload_to='advertisements/')


    @admin.display(description='Дата создания')
    def created_date(self):
        if self.created_at.date()== timezone.now().date():
            created_time = self.created_at.time().strftime('%H:%M:%S')
            return format_html (
            '<span style="color: green; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        else:
            return self.created_at.strftime('%d.%m.%Y в %H:%M:%S')

    @admin.display(description='Дата обновления')
    def updated_date(self):
        if self.updated_at.date() == timezone.now().date():
            created_time = self.updated_at.time().strftime('%H:%M:%S')
            return format_html(
                '<span style="color: purple; font-weight: bold;">Сегодня в {}</span>', created_time
            )
        else:
            return self.updated_at.strftime('%d.%m.%Y в %H:%M:%S')


    @admin.display(description='Фотография')
    def get_html_image(self):
        if self.image:
            return format_html('<img scr="{url}" style=" max-width: 60px; max-height: 60px;">', url=self.image.url)

    class Meta:
        db_table = 'advertisements'

    def __str__(self):
        return  ('id='+ str(self.id) + ', '+ 'title='+ self.title+', '+'price='+ str(self.price))


