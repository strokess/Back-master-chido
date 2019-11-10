from django.contrib import admin  
from django.urls import path  
from employee import views  

urlpatterns = [  
    path('',views.login, name="login"),
    path('visitas/',views.visitas, name="visitas"),
    path('visitas2/',views.visitas2, name="visitas2"),
    path('clientes/', views.clientes, name="clientes"),
    path('compras/', views.compras, name="compras"),
    path('ventas/', views.ventas, name="ventas"),
    path('reportes/', views.reportes, name="reportes"),
    path('admin/', admin.site.urls),  
    path('emp', views.emp),  
    path('show',views.show),  
    path('edit/<int:id>', views.edit),  
    path('update/<int:id>', views.update),  
   path('delete/<int:id>', views.destroy),  
]
