from django.db import models


class Category(models.TextChoices):
    tech = 'TC', 'Tecnologia'
    cr = 'CR', 'Curiosidades'
    geral = 'GR', 'Geral'
    
class Contact(models.Model):
    name = models.CharField(max_length=150)
    email = models.EmailField()
    message = models.TextField()
    
    def __str__(self):
        return self.name
    
class Post(models.Model):
    title = models.CharField(max_length=200)
    sub_title = models.CharField(max_length=200)
    content = models.TextField()
    categories = models.CharField(
       max_length = 2,
       choices = Category.choices,
       default = Category.geral, 
    )
    
    approved = models.BooleanField(default=True)
    imagem = models.ImageField(upload_to='posts', null=True, blank=True)
    
    def __str__(self):
        return self.title
    
    def full_name(self):
        return self.title + self.sub_title
    
    def get_category_label(self):
        return self.get_categories_display()
    
    full_name.admin_order_field = 'title'