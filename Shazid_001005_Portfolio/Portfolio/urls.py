from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', register, name='register'),
    path('SignIn/', SignIn, name='SignIn'),
    path('home/', home, name='home'),
    path('logout_f/', logout_f, name='logout_f'),
    path('profile/', profile, name='profile'),
    path('user_profile_update/', user_profile_update, name='user_profile_update'),
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
