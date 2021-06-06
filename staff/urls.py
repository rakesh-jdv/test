from django.urls import path
from staff import views

urlpatterns = [
    path('', views.liststaffApiView.as_view(), name = 'staff_list'),
    path('create/', views.createstaffApiView.as_view(), name = 'staff_create'),
    path('update/<int:pk>', views.updatestaffApiView.as_view(), name = 'staff_update'),
    path('delete/<int:pk>', views.deletestaffApiView.as_view(), name = 'staff_delete')
]
