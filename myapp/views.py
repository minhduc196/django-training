from django.shortcuts import render
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.urls import reverse_lazy
from django import forms

from .models import User, Group, Role, UserForm

def index(request):
    return render(request, 'myapp/index.html')
# Create your views here.
class UserIndexView(generic.ListView):
    template_name = 'myapp/user/index.html'
    context_object_name = 'all_users'

    def get_queryset(self):
        return User.objects.all()

class UserDetailView(generic.DetailView):
    model = User
    template_name = 'myapp/user/detail.html'

class UserCreateView(CreateView):
    model = User
    form_class = UserForm
    template_name = 'myapp/user/user_form.html'
    
class UserUpdateView(UpdateView):
    model = User
    template_name_suffix = '_update_form'
    template_name = 'myapp/user/user_update_form.html'
    form_class = UserForm

class UserDeleteView(DeleteView):
    model = User
    template_name = 'myapp/user/user_confirm_delete.html'
    success_url = reverse_lazy('myapp:user-index')

# Views for Role

class RoleIndexView(generic.ListView):
    template_name = 'myapp/role/index.html'
    context_object_name = 'all_roles'

    def get_queryset(self):
        return Role.objects.all()

class RoleDetailView(generic.DetailView):
    model = Role
    template_name = 'myapp/role/detail.html'

class RoleCreateView(CreateView):
    model = Role
    template_name = 'myapp/role/role_form.html'
    fields = [
        'role_name', 'role_desc', 'role_permission'
    ]

class RoleUpdateView(UpdateView):
    model = Role
    template_name_suffix = '_update_form'
    template_name = 'myapp/role/role_update_form.html'
    fields = [
        'role_name', 'role_desc', 'role_permission'
    ]

class RoleDeleteView(DeleteView):
    model = Role
    template_name = 'myapp/role/role_confirm_delete.html'
    success_url = reverse_lazy('myapp:role-index')

# Views for group
class GroupIndexView(generic.ListView):
    template_name = 'myapp/group/index.html'
    context_object_name = 'all_groups'

    def get_queryset(self):
        return Group.objects.all()

class GroupDetailView(generic.DetailView):
    model = Group
    template_name = 'myapp/group/detail.html'

class GroupCreateView(CreateView):
    model = Group
    template_name = 'myapp/group/group_form.html'
    fields = [
        'group_name', 'group_desc', 'group_permission'
    ]

class GroupUpdateView(UpdateView):
    model = Group
    template_name = 'myapp/group/group_update_form.html'
    template_name_suffix = '_update_form'
    fields = [
        'group_name', 'group_desc', 'group_permission'
    ]

class GroupDeleteView(DeleteView):
    model = Group
    template_name = 'myapp/group/group_confirm_delete.html'
    success_url = reverse_lazy('myapp:group-index')
