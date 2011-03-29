from models import Excurtion, PhotoPostExcurtion, Region
from django.contrib import admin

class InlinePhotoPostExcurtionAdmin(admin.TabularInline):
    model = PhotoPostExcurtion
    extra = 3
    max_num = 3

class InlineRegionAdmin(admin.TabularInline):
    model = Region
    extra = 1
    max_num = 1
class ExcurtionAdmin(admin.ModelAdmin):
    model = Excurtion
    inlines = [InlineRegionAdmin, InlinePhotoPostExcurtionAdmin]


admin.site.register(Excurtion, ExcurtionAdmin)
admin.site.register(PhotoPostExcurtion)
admin.site.register(Region)
