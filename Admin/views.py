from django.shortcuts import render,redirect
from Admin.models import*
# Create your views here.
def district(request):
    districtdata=tbl_district.objects.all()
    if request.method == 'POST':
       tbl_district.objects.create(district_name=request.POST.get("txtdis"))
       return render(request,"Admin/District.html",{'data':districtdata})
    else:
       return render(request,"Admin/District.html",{'data':districtdata})

def deldistrict(request,did):
    tbl_district.objects.get(id=did).delete()
    return redirect("webadmin:district")

def category(request):
    categorydata=tbl_category.objects.all()
    if request.method == 'POST':
       tbl_category.objects.create(category_name=request.POST.get("txt_cate"))
       return render(request,"Admin/Category.html",{'data':categorydata})
    else:
       return render(request,"Admin/Category.html",{'data':categorydata})

def delcategory(request,cid):
    tbl_category.objects.get(id=cid).delete()
    return redirect("webadmin:category")      

def brand(request):
    branddata=tbl_brand.objects.all()
    if request.method == 'POST':
        tbl_brand.objects.create(brand_name=request.POST.get("txt_brand"))
        return render(request,"Admin/Brand.html",{'data':branddata})
    else:
        return render(request,"Admin/Brand.html",{'data':branddata}) 

def delbrand(request,bid):
    tbl_brand.objects.get(id=bid).delete()
    return redirect("webadmin:brand")  

def size(request):
    sizedata=tbl_size.objects.all()
    if request.method == 'POST':
        tbl_size.objects.create(size_name=request.POST.get("txt_size"))
        return render(request,"Admin/Size.html",{'data':sizedata})
    else:
        return render(request,"Admin/Size.html",{'data':sizedata})

def delsize(request,sid):
    tbl_size.objects.get(id=sid).delete()
    return redirect("webadmin:size")   

def place(request):
    disdata=tbl_district.objects.all()
    return render(request,'Admin/Place.html',{'dis':disdata})

def subcategory(request):
    catedata=tbl_subcategory.objects.create.all()
    return render(request,'Admin/Subcategory.html',{'cate':catedata})    
   
