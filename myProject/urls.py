from django.contrib import admin
from django.urls import path, include

urlpatterns = [ #defines the URL patterns for your application, the urlpatterns list specifies how URLs should be mapped to views
    path("admin/", admin.site.urls),
    path('', include("myApp.urls")), #empty string means patterns will be included at the root level, 'include' includes patterns from another module ('myApp')
]
