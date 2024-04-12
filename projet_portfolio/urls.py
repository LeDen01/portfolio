"""
URL configuration for projet_portfolio project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from about.views import *
from skills.views import *
from portfolio.views import *
from services.views import *
from testimonials.views import *
from contact.views import *

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('admin/', admin.site.urls),    
    path('', index),
    path('administration/', administration),
    path('administration/about/', admin_about),
    path('administration/about/update/', update_about),
    path('administration/skills/', admin_skills),
    path('administration/skills/create/', create_skills),
    path('administration/skills/delete/<int:id>/', delete_skills),
    path('administration/skills/update/<int:id>/', update_skill),
    path('administration/portfolio/', admin_portfolio),
    path('administration/portfolio/delete/<int:id>/', delete_portfolio),
    path('administration/portfolio/create/', create_portfolio),
    path('administration/portfolio/update/<int:id>/', update_portfolio),
    path('administration/services/', admin_services),
    path('administration/services/delete/<int:id>/', delete_services),
    path('administration/services/create/', create_services),
    path('administration/services/update/<int:id>/', update_services),
    path('administration/testimonials/', admin_testimonials),
    path('administration/testimonials/delete/<int:id>/', delete_testimonial),
    path('administration/testimonials/create/', create_testimonial),
    path('administration/testimonials/update/<int:id>/', update_testimonial),
    path('administration/contact/', admin_contact),
    path('administration/contact/update/', update_contact),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
