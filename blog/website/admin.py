from django.contrib import admin
from .models import Post, Contact

class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'sub_title', 'categories', 'approved']
    search_fields = ['title', 'sub_title']
    #fields = ('title', 'sub_title', 'content')
    
    ##def get_queryset(self, request):
    ##    return Post.objects.filter(approved = True)

admin.site.register(Post, PostAdmin)
admin.site.register(Contact)