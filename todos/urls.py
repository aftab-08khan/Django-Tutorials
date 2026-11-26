from . import views
from django.conf import settings
from django.conf.urls.static import static

from django.urls import path

urlpatterns = [path('hello/', views.hello_world, name='hello_world'), 
               path('',views.hello_world_py, name='hello_world_py'), 
               path('html/', views.hello_world_html, name='hello_world_html'),
               path('html/<str:name>', views.hello_world_html_name, name='hello_world_html_name'),
               path('query/',views.hello_world_query, name='hello_world_query'),
               path('redirect/',views.hello_world_redirect, name='hello_world_redirect'),
               path('post/',views.post_examples, name='post_examples'),
               path('submit/',views.submit_examples, name='submit_examples') ,
               path('template/', views.template_view , name='template_view') ,
               path('info/', views.get_info, name='get_info')
               ]



if settings.DEBUG:
    urlpatterns += static(
        settings.MEDIA_URL,
        document_root=settings.MEDIA_ROOT
    )