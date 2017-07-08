from django.contrib.auth.forms import UserCreationForm

from django.contrib.auth.models import User

class UserCreateForm(UserCreationForm):
    class Meta:
        model = User
        fields = ('username','email','password1','password2')
        

    def __init__(self, *args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['username'].label='Display name'
        self.fields['email'].label='email address'
