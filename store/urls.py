from django.urls import path
from django.contrib.auth import views as auth_views
from .views import contact, detail, register, logout_user

from .forms import LoginForm

urlpatterns = [
    path('contact/', contact, name='contact'),
    path('register/', register, name='register'),
    path('login/', auth_views.LoginView.as_view(template_name='store/login.html', authentication_form=LoginForm), name='login'),
    path('logout/', logout_user, name='logout'),
    path('detail/<int:pk>/', detail, name='detail'),
]