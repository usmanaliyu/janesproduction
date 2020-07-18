from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('account/',include('django.contrib.auth.urls')),
    path('account/', include('allauth.urls')),
    path('', include('Account.urls')),
    path('', include('core.urls', namespace='core')),
    path("paystack", include(('paystack.urls', 'paystack'), namespace='paystack')),
]

if settings.DEBUG:
    import debug_toolbar
    urlpatterns += [path('__debug__/', include(debug_toolbar.urls))]
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
