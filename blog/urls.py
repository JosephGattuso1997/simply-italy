from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import path, include

from posts.views import (
    index,
    search,
    post_list,
    post_detail,
    gallery,
    icons,
    Fav,
    filter_by_category,
    Gear,
    IndexView,
    PostListView,
    PostDetailView,
)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', index),
    path('', IndexView.as_view(), name='home'),
    # path('blog/', post_list, name='post-list'),
    path('blog/', PostListView.as_view(), name='post-list'),
    path('icons/', icons, name='icons'),
    path('about/<pk>/', Fav.as_view(), name='about'),
    path('gallery/', gallery, name='gallery'),
    path('Gear/', Gear, name='Gear'),
    # path('post/<id>/', post_detail, name='post-detail'),
    path('post/<pk>/', PostDetailView.as_view(), name='post-detail'),
    # path('post/<id>/update/', post_update, name='post-update'),
    path('blog/<str:category>', filter_by_category, name='filter_by_category'),
    path('tinymce/', include('tinymce.urls')),
    path('accounts/', include('allauth.urls'))
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,
                          document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
