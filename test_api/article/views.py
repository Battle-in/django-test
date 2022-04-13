from django.shortcuts import render
from django.http import  HttpResponse
from article.models import Article
from json import dumps

# Create your views here.
def get_all_articles(request):
    articles = Article.objects.all()
    res = {
        'articles': []
    }
    for i in articles:
        res['articles'].append(i.to_json())
    return HttpResponse(res.__str__())