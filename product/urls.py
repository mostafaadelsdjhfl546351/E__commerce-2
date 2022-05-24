
from django.urls import path,include

from . import views

urlpatterns = [
    path('',views.home,name="home"),
    path('cats',views.AllCategories,name="cats"),
    path('category/<int:categoryid>/',views.Category,name="Category"),
    path('product/<int:productid>/',views.Product,name="Product"),
    
    path('addcart/<int:proid>/', views.addcart, name='addcarts'),
    path('cartitem/', views.cartitem, name='cartitem'),
    path('deleteitem/<int:proid>/', views.deleteitem, name='delete'),
]