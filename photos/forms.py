from django import forms
from photos.models import Photo
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class PhotoAddForm(forms.ModelForm):
    class Meta:
        model = Photo
        fields = '__all__'

    def __init__(self,*args,**kwargs):
        super(PhotoAddForm,self).__init__(*args,**kwargs)
        self.fields['descr'].widget = forms.Textarea(attrs={'placeholder':'Enter a short description'})
        self.fields['descr'].label = 'Description'
        self.fields['category'].empty_label = 'Select a category...'
        self.fields['category'].required= False

class UserRegisterForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['first_name','last_name','username','email','password1','password2']
        
    def __init__(self,*args,**kwargs):
        super(UserRegisterForm,self).__init__(*args,**kwargs)
        self.fields['first_name'].widget = forms.TextInput(attrs={'class' :'form-control'})
        self.fields['last_name'].widget = forms.TextInput(attrs={'class' :'form-control'})
        self.fields['username'].widget = forms.TextInput(attrs={'class' :'form-control'})
        self.fields['email'].widget = forms.EmailInput(attrs={'class' :'form-control'})
        self.fields['password1'].widget = forms.PasswordInput(attrs={'class' :'form-control'})
        self.fields['password2'].widget = forms.PasswordInput(attrs={'class' :'form-control'})
    