from django import forms
from .models import res
from .models import logements
from .models import voitures
from .models import services
#from .models import logementt
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.forms import ModelForm
from django.forms import Form



class SignUpForm(UserCreationForm):
    Nom = forms.CharField(max_length=30, required=False, help_text='Optional.')
    prénom = forms.CharField(max_length=30, required=False, help_text='Optional.')
    Adresse = forms.CharField(max_length=30, required=False, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')

    class Meta:
        model = User
        fields = ('username','Nom', 'prénom', 'Adresse', 'email', 'password1', 'password2', )


class Reservation(ModelForm):
    Nom = forms.CharField(max_length=30, required=True, help_text='Optional.')
    prénom = forms.CharField(max_length=30, required=True, help_text='Optional.')
    Adresse = forms.CharField(max_length=30, required=True, help_text='Optional')
    email = forms.EmailField(max_length=254, help_text='Required. Inform a valid email address.')
    Date_Arrivée = forms.DateField(required=True)
    Date_Départ = forms.DateField(required=True)

    class Meta:
        model = res
        fields = ('Nom', 'prénom', 'Adresse', 'email', 'Date_Arrivée', 'Date_Départ',)



class Log(ModelForm):
    

    class Meta:
        model = logements
        #fields = ('__all__' )
        exclude = ['Photo1', 'Photo2', 'Photo3']

class Voit(ModelForm):
    

    class Meta:
        model = voitures
        #fields = ('__all__' )
        exclude = ['Photo1', 'Photo2', 'Photo3']

class Serv(ModelForm):
    

    class Meta:
        model = services
        #fields = ('__all__' )
        exclude = ['Photo1', 'Photo2', 'Photo3']

