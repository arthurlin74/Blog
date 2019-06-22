from django import forms
from article.models import Article


class ArticleForm(forms.ModelForm):
    title = forms.CharField(label='標題', max_length=128)
    content = forms.CharField(label='內容', widget=forms.Textarea)
#可能會有要填選但不回存項目，例如同意條款
    class Meta:
        model = Article
        fields = ['title', 'content']
        #僅回存這兩個檔案