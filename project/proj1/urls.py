from proj1 import views
from django.views.generic import RedirectView
from django.conf.urls import include,url

app_name='proj1'
urlpatterns=[

              
              url(r'^user_register/',views.user_register,name='user_register'),
              url(r'^user_login/',views.user_login,name='user_login'),
              url(r'^$',views.home1,name='home1'),
              url(r'^proj1/user_login/test/',views.test,name='test'),
              url(r'^questions_list/',views.questions_list,name='questions_list'),
              url(r'^results/',views.results,name='results'),

              
]