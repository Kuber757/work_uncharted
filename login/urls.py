from django.urls import path
from django.contrib.auth.views import LogoutView
from . import views

app_name = 'login'

urlpatterns = [
    path('login', views.LoginView.as_view(),name='login'),
    path('signup', views.SignUpView.as_view(),name='signup'),
    path('logout', LogoutView.as_view(), name='logout'),
    path('projects/', views.projects,name='projects'),
    path('materials/', views.materials,name='materials'),
    path('collections/', views.collections,name='collections'),
    path('projects-detail/', views.project_detail,name='projects-detail'),
    path('materials-detail/', views.material_detail,name='materials-detail'),
    path('collections-detail/', views.collection_detail,name='collections-detail'),
    path('', views.menu, name='menu'),
    # path('signup', views.signup,name='signup'),
    # path('signin', views.signin,name='signin'),
    # path('home', views.home,name='home'),
    path('materials-details/<int:pk>', views.material_details,name='materials-details'),
    path('projects-details/<int:pk>', views.project_details,name='projects-details'),
    path('collections-details/<int:pk>', views.collection_details,name='collections-details'),
    path('details/', views.details,name='details'),
    # path('admin/', admin.site.urls),
]
