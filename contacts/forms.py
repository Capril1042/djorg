from django import forms
from . models import Contact

class ContactForm(forms.ModelForm):
    """form to create contacts"""

    class Meta:
        model = Contact
        fields= ('name', 'email', 'phone', 'address', 'city', 'state', 'zip_code' )