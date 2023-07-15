from django.contrib import admin
from order.models import BirdModel

# Register your models here.
class BirdModelAdmin(admin.ModelAdmin):
    list_display=('id',
                  'name',
                  'familyName',
                  'scientificName',
                  'englishName',
                  'nickName',

                  'level',

                  'startMonth',
                  'endMonth',
                  'season',

                  'habitat',

                  'description',

                  'image',
                  'photoby')
admin.site.register(BirdModel,BirdModelAdmin)
 