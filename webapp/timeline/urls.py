from django.conf.urls import url

from timeline import views


from django.conf import settings
from django.conf.urls.static import static

urlpatterns=[

    url(r'^signup$',views.Signup,name="Signup"),
    url(r'^signin$',views.Signin,name="Signin"),
    url(r'^$',views.dashBoard,name="dashBoard"),
    url(r'^signout$',views.Signout,name="Signout"),
    url(r'^addPosts$',views.model_form_upload,name='addPosts'),
    url(r'^like$',views.like,name='like'),
    # url(r'^comment$',views.commentAdd,name='comment'),
    url(r'^comment/(?P<pk>[0-9]+)$',views.commentAdd,name='comment'),  #()-block (a+b)+(c) <pk> primarykey p is mandidatory


    # url(r'^like/(?P<pk>[0-9]+)$', views.like, name='like'),

]

