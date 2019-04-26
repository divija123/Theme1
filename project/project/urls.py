from django.conf.urls import include , url
from django.contrib import admin
from proj1 import views
from colleges import views
from branches import views


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^colleges/', include('colleges.urls')),
    url(r'^proj1/',include('proj1.urls')),
    url(r'^branches/', include('branches.urls')),
]
