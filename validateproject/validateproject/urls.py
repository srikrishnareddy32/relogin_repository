from django.contrib import admin
from django.conf.urls import url
from validateapp.views import RegForm_Page

urlpatterns = [
    url('admin/', admin.site.urls),
    url(r'^$',RegForm_Page)
]
