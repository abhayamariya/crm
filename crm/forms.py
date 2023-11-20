from django import forms
from crm.models import Employees

from django.contrib.auth.models import User

class EmployeeForm(forms.Form):
    name=forms.CharField()
    department=forms.CharField()
    salary=forms.IntegerField()
    email=forms.CharField()
    age=forms.IntegerField()
    contact=forms.CharField()
    
class EmployeeModelForm(forms.ModelForm):
    class Meta:
        model=Employees
        fields="__all__"


        widgets={

            "name":forms.TextInput(attrs={"class":"form-control"}),
            "department":forms.TextInput(attrs={"class":"form-control"}),
            "salary":forms.NumberInput(attrs={"class":"form-control"}),
            "email":forms.EmailInput(attrs={"class":"form-control"}),
            "age":forms.NumberInput(attrs={"class":"form-control"}),
            "contact":forms.Textarea(attrs={"class":"form-control","row":5}),
            "dob":forms.DateInput(attrs={"class":"form=contyrol","type":"date"})

        

        }
class RegistrationForm(forms.ModelForm):
    class Meta:
        model=User
        fields=["username","email","password"]



class LoginForm(forms.Form):
    username=forms.CharField(widget=forms.TextInput(attrs={"class":"form-control"}))
    password=forms.CharField(widget=forms.PasswordInput(attrs={"class":"form-control"}))
            
        





            
            

        
        
     



