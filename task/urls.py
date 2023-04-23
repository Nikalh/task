from django.contrib import admin
from django.urls import path, include

from task.network import views

urlpatterns = [
    path('users/', include(('task.users.urls', 'task.users'))),
    path('admin/', admin.site.urls),
    path('supplier/', include(('task.network.urls', 'task.network'))),
    path('factory/',  include(('task.factory.urls', 'task.factory'))),
    path('retailnet/',  include(('task.retail.urls', 'task.retail'))),
    path('product/',  include(('task.product.urls', 'task.product'))),


]
