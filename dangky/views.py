from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from dangky.models import NguoiDung

# Create your views here.
def dangky(request):
    return render (request,'dangky.html')
def home(request):
    return render(request,'home.html')
def thatbai(request):
    return render(request, 'thatbai.html')
def taotk(request):
    ten = request.GET.get('ten')
    mail = request.GET.get('mail')
    matkhau = request.GET.get('matkhau')
    if((len(ten)>10) & ("@" in mail)):
        data = NguoiDung(
            ten_dang_nhap = ten,
            email = mail,
            mat_khau = matkhau
            
        )
        data.save()
        return render(request,'dangnhap.html')
    
    else: 
        return render(request, 'thatbai.html')
    
    # if (len(str(ten)) > 10) & (str(mail).count("@")>0):
    #     return render(request,'dangnhap.html')
    # else: return render(request, 'thatbai.html')
    
       