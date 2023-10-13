from django import forms 
from Apiapp.models import User

class UserForm(forms.ModelForm):
    class Meta:
        model=User
        fields=['task_title' , 'task_desc']