from django.db import models
from account.models import User


class Article(models.Model):
    title = models.CharField(max_length=128, unique=True) #128 = 字數，與bit樹無關，unique 項目唯一性，在此因文章標題為唯一性，故為 True
    content = models.TextField()
    pubDateTime = models.DateTimeField(auto_now_add=True)
    likes = models.ManyToManyField(User)
    
    def __str__(self):
        return self.title #回去看工研院講義第五章
    class Meta:
        ordering = ['-pubDateTime']


class Comment(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    # on_delete=models.CASCADE 表示「連串刪除」，亦即當所指的外來資料刪除時，本資料一併刪除。 所以，當某篇文章刪除時，Django 會將該文章的所屬的所有留言一併刪除
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    content = models.CharField(max_length=128)
    pubDateTime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.article.title + '-' + str(self.id)
        
        class Meta:
            ordering = ['pubDateTime']