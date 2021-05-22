from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views

app_name = 'Blog'
urlpatterns = [
    path('',views.HomeView,name='HomeView'),
    # My Blogs
    path('myblogs/',views.MyBlogs,name='MyBlogs'),
    # Add New Blog
    path('newblog/',views.AddBlog,name='AddBlog'),
    # See Blogs
    path('Blog/<slug>',views.BlogView,name='BlogView'),
    # Edit Blog
    path('EditBlog/<slug>',views.EditBlog,name='EditBlog'),
    # Search Blogs
    path('Search/',views.SearchBlog,name='SearchBlog'),

]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)