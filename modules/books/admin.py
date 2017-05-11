from django.contrib import admin
from .models import Book,Comments

class BookAdmin(admin.ModelAdmin):
    pass

class CommentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book, BookAdmin)
admin.site.register(Comments,CommentAdmin)
