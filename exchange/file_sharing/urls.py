from django.urls import path, include
from django.views.decorators.cache import cache_page  # импорт для кеширования

from .views import *

urlpatterns = [
    #path('', cache_page(60)(RecordHome.as_view()), name='home'),  # пример кеширования
    path('', RecordHome.as_view(), name='home'),
    # path('', index, name='home'),
    path('about/', about, name='about'),
    # path('addpage/', addpage, name='add_page'),
    path('login/', LoginUser.as_view(), name='login'),
    path('logout/', logout_user, name='logout'),
    path('contact/', contact, name='contact'),
    path('post/<slug:post_slug>', ShowPost.as_view(), name='post'),
    #path('post/<slug:post_slug>', show_post, name='post'),
    path('discipline/<slug:discipline_slug>', RecordDiscipline.as_view(), name='discipline'),
    #path('discipline/<int:discipline_id>', show_discipline, name='discipline'),
]
