from django import forms

from .models import User, Group, Role

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'firstname', 'lastname', 'birthday', 'password', 'hobbies', 'user_desc'
        )
        widgets = {
            'firstname' : forms.Textarea(),
        }

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name', 'group_desc', 'group_permission'
        ]

class RoleForm(forms.ModelForm):
    model = Role
    fields = [
        'role_name', 'role_desc', 'role_permission'
    ]