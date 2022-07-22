from django.contrib import admin
from django.urls import path,include
from nhanvien import views

urlpatterns = [
    path('', views.bangnhanvien),
    path('themnhanvien/',views.themnhanvien,name="themnhanvien"),
    path('them_nhan_vien/',views.them_nhan_vien,name="them_nhan_vien"),
    path('<int:id_nv>/',views.chi_tiet, name="chi_tiet"),
    path('xuly_capnhat/',views.xuly_capnhat,name="xuly_capnhat"),
    path('xoa_nhanvien/<int:id_nv>/',views.xoa_nhanvien,name="xoa_nhanvien"),
]