from django.urls import path
from . import views


urlpatterns = [
    path("signup/", views.SignUpView.as_view(),name="signup"),
    path("addsale/",views.addsale,name="addsale"),
    path("",views.listsale,name="listsale"),
    path("deletesale/<int:id>",views.deletesale,name="deletesale"),
    path("mycart/",views.mycart,name="mycart"),
    path("add/<int:id>",views.addcart,name="addcart"),
    path("delete/<int:id>",views.deleteshop,name="deleteshop")
]
