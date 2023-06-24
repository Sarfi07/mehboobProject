from django.urls import path

from . import views

urlpatterns = [
    path("", views.index_view, name="index"),
    path("render/<str:name>", views.htmlRender, name="htmlRender"),
    path("register", views.register, name="register"),
    path('login', views.login_view, name="login"),
    path('logout', views.logout_view, name="logout"),
    path('studentAddmission', views.studentAddmission_view, name="studentAddmission"),
    path('contactRequest', views.contactRequest_view, name="contactRequest")

]