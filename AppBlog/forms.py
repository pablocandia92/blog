#from django.contrib.auth.forms import UserCreationForm, AuthenticationForm, UsernameField
#from django.contrib.auth.models import User
from django import forms
#from django.core.exceptions import ValidationError
#from django.utils.translation import gettext_lazy
from .models import *


class FormularioComentario(forms.Form):


    texto=forms.CharField(widget=forms.Textarea())

    