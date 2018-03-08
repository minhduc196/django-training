from django.db import models
from django import forms
from django.urls import reverse

from django.utils.translation import gettext_lazy as _

# Create your models here.
class User(models.Model):
    firstname = models.CharField(max_length=100)
    lastname = models.CharField(max_length=100)
    fullname = models.CharField(max_length=201, default=0)
    password = models.CharField(max_length=100)
    birthday = models.DateField('birthday')
    hobbies = models.TextField()
    user_desc = models.TextField()

    def get_absolute_url(self):
        return reverse('myapp:user-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.fullname + self.birthday

    def save(self, *args, **kwargs):
        self.getfullname()
        super().save(*args, **kwargs)

    def getfullname(self):
        self.fullname = self.firstname + " " + self.lastname

class DateInput(forms.DateInput):
    input_type = 'date'
    
class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = (
            'firstname', 'lastname', 'birthday', 'password', 'hobbies', 'user_desc'
        )
        widgets = {
            'firstname' : forms.TextInput(attrs={'class': 'form-control'}),
            'lastname' : forms.TextInput(attrs={'class': 'form-control'}),
            'password' : forms.PasswordInput(attrs={'class': 'form-control'}),
            'birthday' : DateInput(attrs = {'class' : 'form-control' }),
            'hobbies' : forms.Textarea(attrs={'class': 'form-control'}),
            'user_desc' : forms.Textarea(attrs={'class': 'form-control'}) 
        }
        
class Group(models.Model):
    GROUP_PERMISSION_CHOICES = (
        ('ADD', 'ADDNEW'),
        ('EDIT', 'EDIT'),
        ('DEL', 'DELETE')
    )
    group_name = models.CharField(max_length=50)
    group_permission = models.CharField(
        max_length=4,
        choices=GROUP_PERMISSION_CHOICES,
    )
    group_desc = models.TextField()
    user = models.ManyToManyField(User)

    def __str__(self):
        return self.group_name + self.group_desc
    
    def get_absolute_url(self):
        return reverse('myapp:group-detail', kwargs={'pk': self.pk})

class GroupForm(forms.ModelForm):
    class Meta:
        model = Group
        fields = [
            'group_name', 'group_desc', 'group_permission'
        ]

class Role(models.Model):
    ROLE_PERMISSION_CHOICE = (
        ('ADMIN', 'ADMIN'),
        ('PUBLISHER', 'PUBLISHER'),
        ('APPROVER', 'APPROVER'),
        ('MODERATOR', 'MODERATOR'),
        ('EDITOR', 'EDITOR'),
        ('CREATOR', 'CREATOR'),
    )
    role_name = models.CharField(max_length=100)
    role_permission = models.CharField(
        max_length=10,
        choices=ROLE_PERMISSION_CHOICE,
    )
    role_desc = models.TextField()
    
    user = models.ManyToManyField(User)

    def get_absolute_url(self):
        return reverse('myapp:role-detail', kwargs={'pk': self.pk})

    def __str__(self):
        return self.role_name + self.role_desc

class RoleForm(forms.ModelForm):
    model = Role
    fields = [
        'role_name', 'role_desc', 'role_permission'
    ]