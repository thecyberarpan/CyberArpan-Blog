from django.urls import path
from . import views

urlpatterns = [
    path("", views.Index, name = "Index"),
    path("register/", views.Register, name = "Register"),
    path("login/", views.Login, name = "Login"),
    path("logout/", views.Logout, name = "Logout"),
    path("upload-post/", views.UploadPost, name = "UploadPost"),
    path("blog-detail/<int:id>", views.BlogDetail, name = "BlogDetail"),
    path("delete/<int:id>", views.Delete, name = "Delete"),
    path("edit-blog/<int:id>", views.EditBlog, name = "EditBlog"),
]