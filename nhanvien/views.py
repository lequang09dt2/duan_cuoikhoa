from django.shortcuts import render, get_object_or_404
from django.http import HttpRequest,HttpResponse
from nhanvien.models import NhanVien
from django.template import loader

# Create your views here.
#hàm này hiển thị giao diện thêm nhân viên
def themnhanvien(request):
    return render (request,'themnhanvien.html')

def bangnhanvien(request):
    bang = NhanVien.objects.all().values()
    template = loader.get_template('bangnhanvien.html')
    context = {
        'bang': bang,
    }
    return HttpResponse(template.render(context, request))

#Hàm này thực hiện thêm nhân viên vào CSDL
def them_nhan_vien(request):
    ten = request.GET.get('tennhanvien')
    chuc_vu = request.GET.get('chucvu')
    nam_sinh = request.GET.get('namsinh')

    if((len(ten)>1)&(chuc_vu!="")&(nam_sinh!="")):
        dulieu = NhanVien(
            ten_nhan_vien = ten,
            chucvu = chuc_vu,
            namsinh = nam_sinh,
            
        )
        dulieu.save()
        bang = NhanVien.objects.all().values()
        context = {
            'bang': bang,
        }
        return render(request, 'bangnhanvien.html',context)
    
    else: 
        return render(request, 'them_nv_loi.html')
    
    
def chi_tiet(request,id_nv):
    nv= get_object_or_404(NhanVien,pk = id_nv)
    context = {
        'nhan_vien':nv
    }
    return render(request,'chitiet.html',context)

def xuly_capnhat(request):
    ten = request.GET.get('tennhanvien')
    chuc_vu = request.GET.get('chucvu')
    nam_sinh = request.GET.get('namsinh')
    id_nv = request.GET.get('id_nv')
    
    NhanVien.objects.filter(id = id_nv).update(
        ten_nhan_vien = ten,
        chucvu = chuc_vu,
        namsinh = nam_sinh,)
            
    nhan_vien = NhanVien.objects.all()
    context = {
        'bang': nhan_vien,
    }
    return render(request, 'bangnhanvien.html',context)
    
def xoa_nhanvien(request,id_nv):
    nv= get_object_or_404(NhanVien,pk = id_nv)
    try:
        nv.delete()
    except:
        print("xóa lỗi")
    nhan_vien = NhanVien.objects.all()
    context = {
        'bang': nhan_vien,
    }
    return render(request, 'bangnhanvien.html',context)