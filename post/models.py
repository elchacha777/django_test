from django.db import models


class Category(models.Model):
    category = models.CharField(max_length=100)

    class Meta:
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self) -> str:
        return self.category
    
class Post(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE,
    blank=True, null=True, related_name='posts') 
    title = models.CharField(max_length=240)
    body = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)


    class Meta:
        verbose_name = 'Посты'
        verbose_name_plural = 'Посты'

    def __str__(self) -> str:
        return self.title
