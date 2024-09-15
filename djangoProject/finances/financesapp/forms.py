from django import forms
from financesapp.models import Form, Posts

class SignUP(forms.ModelForm):
    class Meta:
        model = Form
        fields = '__all__'
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'User','autocomplete':'off'}),
            'password': forms.PasswordInput(attrs={'placeholder': 'Password'}),
        }

class AddPostForm(forms.ModelForm):
    class Meta:
        model = Posts
        fields = [
            'title', 
            'text'
            ]
        exclude = ['author']
        widgets = {
            'title': forms.TextInput(attrs={'placeholder': 'Título', 'autocomplete':'off'}),
            
            'text': forms.TextInput(attrs={'placeholder': 'Texto'})
        }
 #   '__all__'
       
#'author': forms.TextInput(attrs={'placeholder': 'Author'}),