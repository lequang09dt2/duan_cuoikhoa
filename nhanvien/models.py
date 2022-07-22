from django.db import models

# Create your models here.
class NhanVien(models.Model):
    ten_nhan_vien = models.CharField(max_length= 100)
    chucvu = models.CharField(max_length= 100)
    namsinh = models.CharField(max_length= 4)
    
    def __str__(self):
        return self.ten_nhan_vien
        
