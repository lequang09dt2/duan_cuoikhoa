from django.contrib import admin
from django.urls import path,include
from dangnhap import views


urlpatterns = [
    path('', views.dangnhap),
    path('xuly_dangnhap/',views.xuly_dangnhap,name="xuly_dangnhap"),
    path('bangnhanvien/', include('nhanvien.urls')),
    # path('them_nhan_vien/', include('nhanvien.urls')),
]