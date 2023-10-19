from . import views
from django.urls import path

urlpatterns = [
    path('', views.index, name='index'),
    path('register', views.register, name='register'),
    path('log', views.log, name='log'),
    path('logout', views.logout, name='logout'),
    path('newpage', views.newpage, name='newpage'),
    path('form', views.user_form, name='user_form'),
    path('departments', views.departments, name='departments'),
    path('courses', views.courses, name='courses'),
    path('materials_provided', views.materials_provided, name='materials_provided'),
    path('orderconfirm', views.orderconfirm, name='orderconfirm'),
    # path('user_profile/<int:user_id>/', views.user_profile, name='user_profile'),
]
