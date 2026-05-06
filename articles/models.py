from django.db import models

# Create your models here.
class Category (models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField(unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Article(models.Model):
    STATUT_CHOICES = [
        ('draf', 'Draft') ,
        ('published', 'Published') ,
    ]

    title = models.CharField(max_length=200)
    content = models.TextField()
    category = models.ForeignKey( Category, on_delete=models.CASCADE, related_name='articles')
    author = models.CharField(max_length=100)
    statut = models.CharField(max_length=10, choices=STATUT_CHOICES, default='draft')
    published_at = models.DateTimeField(null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
       return self.title
    
    class Meta:
        ordering = ['-created_at']
    