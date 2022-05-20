from django.db import models

class Post(models.Model):
    title = models.CharField(verbose_name='Название', max_length=250)
    desc = models.TextField(verbose_name='описание', max_length=200)
    author = models.CharField(verbose_name='Автор', max_length=200)


class Comment(models.Model):
    user_comment = models.CharField(verbose_name='Комментарий',max_length=100)
    author = models.CharField(verbose_name="Автор", max_length=100)



