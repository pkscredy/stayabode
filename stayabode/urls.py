"""stayabode URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin

from td_list.views import (AllToDoView, ModifyTicketView, TicketActivityView,
                           TicketHtmlView)

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^get_tickets/$', TicketActivityView.as_view(), name='get_tickets'),
    url(r'^raise_ticket/$', TicketHtmlView.as_view(), name='raise_ticket'),
    url(r'^update_ticket/(?P<ticket_uuid>[0-9a-z-]+)/$',
        ModifyTicketView.as_view(), name='update_ticket'),
    url(r'^modify_ticket/(?P<ticket_uuid>[0-9a-z-]+)/$',
        ModifyTicketView.as_view(), name='modify_ticket'),
    url(r'^all_todo/$', AllToDoView.as_view(), name='get_all'),
]
