from django.contrib import admin
from photos.models import Category,Photo

# Register your models here.
@admin.register(Category)
class CatReg(admin.ModelAdmin):
    list_display = ['name']

@admin.register(Photo)
class PhotoReg(admin.ModelAdmin):
    list_display = ['descr','category','image']