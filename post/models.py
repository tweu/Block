from django.db import models
from django.conf import settings
from django.db.models.deletion import CASCADE, PROTECT
from django.urls import reverse

# Create your models here.


class Tag(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='Слаг')

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Tag'
        verbose_name_plural = 'Tags'


class Category(models.Model):

    title = models.CharField(max_length=100, verbose_name='Название')
    slug = models.SlugField(verbose_name='Слаг')

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('posts_by_category', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Category'
        verbose_name_plural = 'Categories'


class Post(models.Model):

    title = models.CharField(max_length=250, verbose_name='Заголовок')
    content = models.TextField(verbose_name='Контент')
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=PROTECT, verbose_name='Автор', related_name= 'posts')
    category = models.ForeignKey(
        Category, on_delete=CASCADE, verbose_name='Категория', related_name='posts')
    tags = models.ManyToManyField(Tag, verbose_name='Тэги')
    created_at = models.DateTimeField(
        auto_now_add=True, verbose_name='Опубликовано')
    slug = models.SlugField(verbose_name='Слаг')
    views = models.PositiveIntegerField(default=0, verbose_name= 'Количество просмотров')
    photo = models.ImageField(upload_to = 'posts/%Y/%m/%d/', verbose_name='Фото', null = True, blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('post_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'
