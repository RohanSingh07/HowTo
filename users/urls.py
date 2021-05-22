from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from . import views
app_name = 'users'

urlpatterns = [
    # Signup
    path('signup/',views.Signup,name='Signup'),
    # Login
    path('login/',views.Login,name='login'),
    # Logout
    path('logout',views.Logout,name='logout'),

]


if settings.DEBUG:
    urlpatterns+=static(settings.STATIC_URL,document_root = settings.STATIC_ROOT)

    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)