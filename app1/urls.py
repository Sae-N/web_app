from django.conf.urls import url
from django.contrib import admin

import app1.views as manager_view


urlpatterns = [
    url('admin/', admin.site.urls),
    url('index/', manager_view.WorkerListView.as_view())
]
 
