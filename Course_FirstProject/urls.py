from django.urls import include, path # Import include and path function 
from django.contrib import admin

urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('blog.urls')),  # Include blog app URLs 
]
