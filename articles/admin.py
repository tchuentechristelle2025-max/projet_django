from django.contrib import admin
from articles.models import Article, Category

# Register your models here.
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ('name', 'slug', 'created_at')
    search_fields = ('name', 'slug',)
    prepopulated_fields = {'slug': ('name' ,)}

@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    list_display = ('title', 'content', 'category', 'author', 'statut', 'published_at')
    list_filter = ('statut', 'published_at',)
    search_fields = ('title', 'content', 'author')  