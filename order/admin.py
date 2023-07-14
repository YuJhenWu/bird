from django.contrib import admin
from order.models import BirdModel

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
 