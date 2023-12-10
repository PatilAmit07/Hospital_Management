from django import forms
from .models import  a1,a2
# class b1(forms.Form):
#     Email=forms.EmailField(max_length=30)
#     Password=forms.CharField(widget=forms.PasswordInput)

class b2(forms.ModelForm):
    class Meta:
        model=a1
        fields='__all__'

class b3(forms.ModelForm):
    class Meta:
        model=a2
        fields='__all__'