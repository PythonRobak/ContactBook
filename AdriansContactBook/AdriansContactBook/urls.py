"""AdriansContactBook URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path, re_path
from ContactBook.views import main_window_view, show_group_view, add_group_view, show_groups_view, delete_group_view, \
    add_member_view, delete_member_view, show_member_view, modify_member_view, add_to_group_view, \
    remove_from_group_view, show_address_view

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_window_view),
    re_path(r'^new$', add_member_view),
    re_path(r'^modify/(?P<member_number>(\d)+)$', modify_member_view),
    re_path(r'^delete/(?P<member_number>(\d)+)$', delete_member_view),
    re_path(r'^show/(?P<member_number>(\d)+)$', show_member_view),
    re_path(r'^addDetails/(?P<member_number>(\d)+)$', show_address_view),
    re_path(r'^browseGroups/$', show_groups_view),
    re_path(r'^addGroup/$', add_group_view),
    re_path(r'^showGroup/(?P<group_number>(\d)+)$', show_group_view),
    re_path(r'^deleteGroup/(?P<group_number>(\d)+)$', delete_group_view),
    re_path(r'^addToGroup/(?P<member_number>(\d)+)$', add_to_group_view),
    re_path(r'^removeFromGroup/(?P<member_number>(\d)+)$', remove_from_group_view),
    # re_path(r'^addedToGroups/(?P<member_number>(\d)+)$', add_to_group_view),

]


