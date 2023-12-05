from django import forms
from .models import Reg, Contact

class RegForm(forms.ModelForm):
    class Meta:
        model = Reg
        fields = "__all__"

class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"
