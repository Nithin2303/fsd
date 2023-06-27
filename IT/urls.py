

from django.urls import path
from IT import views

from IT.views import studentreg,studentlist,studentdetail,studentupdate,studentdelete

app_name = "IT"
urlpatterns = [
    path('',views.Home,name = 'Home'),
    path('services',views.services,name = 'services'),
    path('contact',views.contact,name='contact'),
    path('about',views.about,name = 'about'),

    path('studentreg',studentreg.as_view(),name = 'studentreg'),
    path('<pk>/studentdetail',studentdetail.as_view(),name = 'studentdetail'),
    path('',studentlist.as_view(),name = 'studentlist'),
    path('<pk>/studentupdate',studentupdate.as_view(),name = 'studentupdate'),
    path('<pk>/studentdelete',studentdelete.as_view(),name = 'studentdelete'),

    path('student',views.student, name = 'student'),
    path('form', views.form,name  = 'form'),
    path('detail/<int:id>', views.detail, name = 'detail'),
    path('update/<int:id>', views.update, name = 'update'),
    path('delete/<int:id>', views.delete, name = 'delete'),

    path('rit',views.rit, name = ''),
    path('get1', views.get1, name = 'get1'),
    path('post1', views.post1, name = 'post1'),

    path('index', views.index, name = 'index'),
    path('about', views.about, name = 'about'),
    path('blog', views.blog, name = 'blog'),
    path('contact', views.contact, name = 'contact'),
    path('portfolio', views.portfolio, name = 'portfolio'),
    path('blog_single', views.blog_single, name = 'blog_single'),

    path('register', views.register, name = 'register'),
    path('login_reg', views.login_reg, name = 'login'),
    path('logout', views.logoutuser, name = 'logout'),
]





