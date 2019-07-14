from django.urls import path
from . import views 
urlpatterns = [
    path('',views.home ,name = 'home'),
    path('login/',views.login_user, name='login'),
    path('logout/',views.logout_user, name='logout'),
    path('register/',views.register_user, name='register'),
    path('edit_profile/',views.edit_profile, name='edit_profile'),
    path('change_password/',views.change_password, name='change_password'),
    path('About_Us/',views.About_Us, name= 'About_Us'),
    path('Services/',views.Services, name='Services'),
    path('Contact_Us/',views.Contact_Us, name='Contact_Us'),
]
