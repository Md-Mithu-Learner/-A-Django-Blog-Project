
from django.contrib import admin
from django.urls import path, include
from App_Login import urls as login_urls
from App_Blog import urls as blog_urls
from .views import index
from django.conf import settings
from django.contrib.staticfiles.urls import static, staticfiles_urlpatterns

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/', include(login_urls, namespace='App_Login')),
    path('blog/', include(blog_urls, namespace='App_Blog')),
    path('', index, name='index'),
]

urlpatterns += staticfiles_urlpatterns()
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
