from django.contrib import admin
from django.urls import path
from . import views

# Django Admin Header Customization.

admin.site.site_header = "Government Website Link Administration"
admin.site.site_title = "Website | Nepal | Admin"
admin.site.index_title = "Website | Nepal | Portal"

urlpatterns = [
    path('', views.home, name='home'),
    path('gov_forms', views.gov_forms, name='gov_forms'),
    path('provinces', views.provinces, name='provinces'),
    path('metropolitans', views.metropolitans, name='metropolitans'),
    path('sub_metropolitans', views.sub_metropolitans, name='sub_metropolitans'),
    path('municipalities', views.municipalities, name='municipalities'),
    path('rural_municipalities', views.rural_municipalities, name='rural_municipalities'),
    path('contact', views.contact, name='contact'),
    path('Social_Media', views.Social_Media, name='Social_Media')
]