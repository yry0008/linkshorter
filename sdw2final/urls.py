"""sdw2final URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from django.conf.urls.static import static
from links import views
from sdw2final import settings
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.create, name='create'),
    path('do_create',views.do_create,name='do_create'),
    path('about/',views.about,name='about'),
    path('stat/',views.stat,name='stat'),
    path('do_delete',views.do_delete,name='do_delete')] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT) + [path('<token>/', views.index, name='index')
]
