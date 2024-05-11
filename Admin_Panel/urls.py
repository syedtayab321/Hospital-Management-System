from django.urls import path
from Admin_Panel import views

urlpatterns = [
    path('',views.index,name=('/')),
    path('admin_login',views.admin_login,name=('admin_login')),
    path('admin_dashboard',views.admin_dashboard,name=('admin_dashboard')),
    path('forgot_password',views.forgot_password,name=('forgot_password')),
    path('add_doctor',views.add_doctor,name=('add_doctor')),
]
