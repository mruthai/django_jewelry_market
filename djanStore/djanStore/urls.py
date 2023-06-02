from django.conf import settings     # This import only needed during development to display images
from django.conf.urls.static import static # this import is only needed during development to display images


from django.contrib import admin
from django.urls import path, include




urlpatterns = [
    path('', include('core.urls')),
    path('dashboard/', include('dashboard.urls')),
    path('items/', include('item.urls')),
    path('inbox/', include('conversation.urls')),
    path('admin/', admin.site.urls),
]    + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) # This line of code points to the media folder & only used in development
  