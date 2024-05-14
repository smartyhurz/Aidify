from django.contrib import admin
from django.urls import path
from aidify import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('',views.user_login),
    path('index/',views.view_posts),
    path('about/',views.about),
    path('contact/',views.cont),
    path('editpfp/',views.pfp),
    path('login/',views.user_login,name='login'),
    path('newpost/',views.forse),
    path('signup/',views.register,name='signup'),
    path('user/',views.view_user),
    path('delete/<int:rid>',views.delete),
    path('d/',views.dele),
    path('search/', views.search_results, name='search_results'),
    path('post/<int:post_id>/', views.view_post, name='view_post'),
    path('userlogin/<int:time_id>/',views.datetime),
    
]+ static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
