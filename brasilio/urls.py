from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import RedirectView

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include("api.urls", namespace="api")),
    path("auth/", include("brasilio_auth.urls", namespace="brasilio_auth")),
    path("covid19/", include("covid19.urls", namespace="covid19")),
    path("django-rq/", include("django_rq.urls")),
    path("markdownx/", include("markdownx.urls")),
    path("", include("core.urls", namespace="core")),
    path("favicon.ico", RedirectView.as_view(url=settings.STATIC_URL + "img/favicon.ico")),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

handler403 = "traffic_control.handlers.handler_403"
