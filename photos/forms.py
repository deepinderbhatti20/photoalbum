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
    