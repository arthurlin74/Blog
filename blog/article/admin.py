from django.contrib import admin

# Register your models here.
from article.models import Article, Comment


class CommentModelAdmin(admin.ModelAdmin):
    list_display = ['article', 'content','pubDateTime'] #pubdatetime 講義沒寫
    list_display_links = ['article'] #也可不加
    list_filter = ['article', 'content']
    search_fields = ['content']
    list_editable = ['content']#建議不要加，任意修改太危險
 
    class Meta:
        model = Comment

admin.site.register(Article)
admin.site.register(Comment, CommentModelAdmin)