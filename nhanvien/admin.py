from django.contrib import admin
from nhanvien.models import NhanVien

# Register your models here.
class NhanVienAdmin(admin.ModelAdmin):
    list_display = ('ten_nhan_vien','chucvu', 'namsinh')
    list_display_links = ('ten_nhan_vien','chucvu', 'namsinh')
    list_filter = ('ten_nhan_vien','chucvu', 'namsinh')
    search_fields = ('ten_nhan_vien','chucvu', 'namsinh')
    list_per_page = 25

admin.site.register(NhanVien, NhanVienAdmin)     
    