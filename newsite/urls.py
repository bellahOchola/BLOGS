from django.conf import settings
from django.urls import path, include
from . import views
from django.conf.urls.static import static
from mysite.settings import DEBUG, STATIC_URL, STATIC_ROOT, MEDIA_URL, MEDIA_ROOT
from django.conf.urls.static import static

urlpatterns =[
    path('', views.Index, name='index'),
    path('createblog/', views.CreateBlog, name ='createblog'),
    path('edit_blog/<pk>', views.EditBlog, name ='editblog'),
    path('delete_blog/<pk>', views.DeleteBlog, name ='deleteblog'),
]

if DEBUG:
    urlpatterns += static(STATIC_URL, document_root = STATIC_ROOT)
    urlpatterns += static(MEDIA_URL, document_root = MEDIA_ROOT)