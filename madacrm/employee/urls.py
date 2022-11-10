from django.urls import path
from . import views
urlpatterns = [
    path('homepage',views.homepage,name="mainpage"),
    path('addcoustomer',views.addcoustomer,name="addcoustomer"),
    path('editcoustomer',views.editcoustomer,name="editcoustomer"),
    path('editservices',views.editservices,name="editservices"),
    path('listallservices',views.listallservices,name="listallservices"),
    path('logout',views.logout,name="logout"),
    path('',views.loginpage,name="loginpage")
]
