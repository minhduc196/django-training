from django.urls import re_path
from . import views

app_name = 'myapp'

urlpatterns = [
    re_path(r'^$', views.index, name='index'),
    # url for users management
    re_path(r'^user/$', views.UserIndexView.as_view(), name='user-index'),
    re_path(r'^user/(?P<pk>[0-9]+)/$', views.UserDetailView.as_view(), name='user-detail'),
    re_path(r'^user/(?P<pk>[0-9]+)/update/$', views.UserUpdateView.as_view(), name='user-update'),
    re_path(r'^user/add/$', views.UserCreateView.as_view(), name='user-add'),
    re_path(r'^user/(?P<pk>[0-9]+)/delete/$', views.UserDeleteView.as_view(), name='user-delete'),

    # url for roles management
    re_path(r'^role/$', views.RoleIndexView.as_view(), name='role-index'),
    re_path(r'^role/(?P<pk>[0-9]+)/$', views.RoleDetailView.as_view(), name='role-detail'),
    re_path(r'^role/(?P<pk>[0-9]+)/update/$', views.RoleUpdateView.as_view(), name='role-update'),
    re_path(r'^role/add/$', views.RoleCreateView.as_view(), name='role-add'),
    re_path(r'^role/(?P<pk>[0-9]+)/delete/$', views.RoleDeleteView.as_view(), name='role-delete'),

    #url for groups management
    re_path(r'^group/$', views.GroupIndexView.as_view(), name='group-index'),
    re_path(r'^group/(?P<pk>[0-9]+)/$', views.GroupDetailView.as_view(), name='group-detail'),
    re_path(r'^group/(?P<pk>[0-9]+)/update/$', views.GroupUpdateView.as_view(), name='group-update'),
    re_path(r'^group/add/$', views.GroupCreateView.as_view(), name='group-add'),
    re_path(r'^group/(?P<pk>[0-9]+)/delete/$', views.GroupDeleteView.as_view(), name='group-delete'),
]