from . import views

from django.urls import path

urlpatterns = [path('hello/', views.hello_world, name='hello_world'), path
               ('',views.hello_world_py, name='hello_world_py'), path
               ('html/', views.hello_world_html, name='hello_world_html'),
               path('html/<str:name>', views.hello_world_html_name, name='hello_world_html_name'),
               path('query/',views.hello_world_query, name='hello_world_query'
               ),path('redirect/',views.hello_world_redirect, name='hello_world_redirect')]