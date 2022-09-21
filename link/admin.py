from django.contrib import admin
from link.models import contact
from link.models import home_page, province, metropolitan, sub_metropolitan, municipality, rural_municipality, Social_Media_db, gov_form

# Register your models here.
admin.site.register(contact)
admin.site.register(home_page)
admin.site.register(gov_form)
admin.site.register(province)
admin.site.register(metropolitan)
admin.site.register(sub_metropolitan)
admin.site.register(municipality)
admin.site.register(rural_municipality)
admin.site.register(Social_Media_db)