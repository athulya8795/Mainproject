from django.urls import path
from Admin import views
app_name="webadmin"
urlpatterns = [
    path('district/',views.district,name="district"),
    path('deldistrict/<int:did>',views.deldistrict,name="deldistrict"),

    path('category/',views.category,name="category"),
    path('delcategory/<int:cid>',views.delcategory,name="delcategory"),

    path('brand/',views.brand,name="brand"),
    path('delbrand/<int:bid>',views.delbrand,name="delbrand"),

    path('size/',views.size,name="size"),
    path('delsize/<int:sid>',views.delsize,name="delsize"),

    path('place/',views.place,name="place"),

    path('subcategory/',views.subcategory,name="subcategory"),
]