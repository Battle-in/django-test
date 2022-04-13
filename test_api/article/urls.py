from django.contrib import admin
from django.urls import path

from article.views import *

articles_urls = [
    path('all/', get_all_articles)
]