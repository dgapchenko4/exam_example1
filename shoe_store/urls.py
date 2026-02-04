from django.contrib import admin
from django.urls import path, include
from django.contrib.auth import views as auth_views
from products.views import product_list
from accounts.views import register_view  # импортируем представление регистрации

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', product_list, name='home'),
    
    # Аутентификация (встроенные представления Django)
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='home'), name='logout'),
    
    # Регистрация (наше кастомное представление)
    path('register/', register_view, name='register'),
    
    # Приложения (если есть)
    path('products/', include('products.urls')),
    path('orders/', include('orders.urls')),
]
