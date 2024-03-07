from django.contrib import admin
from django.urls import path,include
from rest_framework import routers
from rest_framework.urlpatterns import format_suffix_patterns
from store import views

user_list = views.UserViewSet.as_view({ 'get': 'list'})
user_detail = views.UserViewSet.as_view({'get': 'retrieve'})
user_byname = views.UserViewSet.as_view({'get': 'getbyname'})

client_list = views.ClientViewSet.as_view({
    'get': 'list',
    'post': 'create'
})
client_detail = views.ClientViewSet.as_view({
    'get': 'retrieve',
    'put': 'update',
    'patch': 'partial_update',
    'delete': 'destroy'
})

client_byname = views.ClientViewSet.as_view({'get': 'getbyname'})

urlpatterns = [
    path('',views.SkuList.as_view()),
    path('api-auth/', include('rest_framework.urls')),
    path('admin/', admin.site.urls),
    path('sku/', views.SkuList.as_view()),
    path('sku/<int:pk>/', views.SkuDetail.as_view()),
    path('transactions/', views.TransactionList.as_view()),
    path('transaction/<int:pk>/', views.TransactionDetail.as_view()),
    path('orders/', views.OrderList.as_view()),
    path('order/<int:pk>/', views.OrderDetail.as_view()),

    path('users/', user_list, name='user-list'),
    path('user/<int:pk>/', user_detail, name='user-detail'),
    path('user/<str:username>',user_byname,name="user-byname"),
    path('clients/',client_list, name="client-list"),
    path('client/<int:pk>',client_detail, name="client-detail"),
    path('client/<str:name>',client_byname,name="client-byname")

]


urlpatterns = format_suffix_patterns(urlpatterns)