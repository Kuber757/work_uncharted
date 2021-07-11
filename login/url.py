from django.urls import path
from . import views

urlpatterns = [
    path('', views.loginpage,name='loginpage'),
    path('projects/', views.projects,name='projects'),
    path('materials/', views.materials,name='materials'),
    path('collections/', views.collections,name='collections'),
    path('projects-detail/', views.project_detail,name='projects-detail'),
    path('materials-detail/', views.material_detail,name='materials-detail'),
    path('collections-detail/', views.collection_detail,name='collections-detail'),
    path('menu/', views.menu,name='menu'),
    path('signup', views.signup,name='signup'),
    path('signin', views.signin,name='signin'),
    path('home', views.home,name='home'),
    path('materials-details/<int:pk>', views.material_details,name='materials-details'),
    path('projects-details/<int:pk>', views.project_details,name='projects-details'),
    path('collections-details/<int:pk>', views.collection_details,name='collections-details'),
    path('details/', views.details,name='details'),
    # path('admin/', admin.site.urls),
]
