from django.db import models
from django.forms.models import modelform_factory


class about_me(models.Model):
    text = models.TextField('Обо мне')
    class Meta:
        verbose_name = 'Обо мне'
        verbose_name_plural = 'Обо мне'

def user_directory_path(instance, filename):
    # file will be uploaded to MEDIA_ROOT/user_<id>/<filename>
    return 'user_{0}/{1}'.format(instance.user.id, filename)
class Post_g(models.Model):
    file = models.FileField('Файл', upload_to=user_directory_path)
    pub_date = models.DateField('Дата')
    label = models.CharField('Заголовок',max_length=100)
    text = models.TextField('Описание')
    def __str__(self):
        return self.label
    class Meta:
        verbose_name = 'Пост геометрия'
        verbose_name_plural = 'Посты геометрия'
class Post_a(models.Model):
    file = models.FileField('Файл', upload_to=user_directory_path)
    pub_date = models.DateField('Дата')
    label = models.CharField('Заголовок',max_length=100)
    text = models.TextField('Описание')
    def __str__(self):
        return self.label
    class Meta:
        verbose_name = 'Пост алгебра'
        verbose_name_plural = 'Посты алгебра'

class link_oge_ege(models.Model):
    name = models.TextField('Название')
    url = models.URLField('Ссылка')
    text = models.TextField('Описание')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Ссылка(оге и еге)'
        verbose_name_plural = 'Ссылки(оге и еге)'

class link_interesting(models.Model):
    name = models.TextField('Название')
    url = models.URLField('Ссылка')
    text = models.TextField('Описание')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Ссылка(Это интересно)'
        verbose_name_plural = 'Ссылки(Это интересно)'

class link_olimpiads(models.Model):
    name = models.TextField('Название')
    url = models.URLField('Ссылка')
    text = models.TextField('Описание')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Ссылка(олимпиады)'
        verbose_name_plural = 'Ссылки(олимпиады)'

class liberi(models.Model):
    name = models.TextField('Название')
    text = models.TextField('Описание')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Ссылка(библтоека)'
        verbose_name_plural = 'Ссылки(библиотека)'

class link_uch(models.Model):
    name = models.CharField('Название', max_length=15)
    slug = models.SlugField('Ссылка')
    def __str__(self):
        return self.name
    class Meta:
        verbose_name = 'Ссылка_Меню'
        verbose_name_plural = 'Ссылки_Меню'

class Caruosel(models.Model):
    img = models.ImageField('Картинка', upload_to='C:/Users/lishu/Desktop/Проект/static/images/')
    number = models.IntegerField('Номер слайда')
    class Meta:
        verbose_name = 'Слайд в слайдер'
        verbose_name_plural = 'Слайды в слайдер'

