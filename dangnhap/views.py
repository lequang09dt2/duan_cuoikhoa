from django.shortcuts import render
from dangky.models import NguoiDung
from nhanvien.models import NhanVien
# Create your views here.
def dangnhap(request):
    return render(request,'dangnhap.html')
def xuly_dangnhap(request):
    ten = request.GET.get('ten')
    matkhau = request.GET.get('matkhau')
    thongtin = NguoiDung.objects.filter(ten_dang_nhap = ten, mat_khau = matkhau)
    bang = NhanVien.objects.all().values()
    context = {
        'bang': bang,
    }
    if(thongtin.exists()):
        return render(request,'bangnhanvien.html', context)
    else:
        return render(request,'dang_nhap_loi.html')
# def nhanvien(request):
#     return render(request,'nhanvien.html')