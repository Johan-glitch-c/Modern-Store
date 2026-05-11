from django.contrib import admin
from .models import Product,ProductSize,ProductImage,Category,Size
# Register your models here.
class ProductImagesInLine(admin.TabularInline):
    model = ProductImage
    extra = 1


class ProductSizeInLine(admin.TabularInline):
    model = ProductSize
    extra = 1

class ProductAdmin(admin.ModelAdmin):
    list_display = ['name','category','color','price']
    list_flter=['category','color',]
    serach_fields = ['name','color','description']
    prepopulated_fields = {'slug':('name',)}
    inlines = [ProductImagesInLine,ProductSizeInLine]


class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name','slug']
    prepopulated_fields = {'slug':('name',)}

class SizeAdmin(admin.ModelAdmin):
    list_display = ['name']

admin.site.register(Category,CategoryAdmin)
admin.site.register(Size,SizeAdmin)
admin.site.register(Product,ProductAdmin)