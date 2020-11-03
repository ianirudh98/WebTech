from django import forms
from .models import Address

class AddressForm(forms.ModelForm):
    class Meta:
        model = Address
        fields = [
            'billing_profile',
            "address_line_1",
            'city',
            'state',
            'country',
            'postal_code',
        ]
        widgets = {
            'address_line_1':forms.TextInput(attrs={"class":"form-control col-6","placeholder":"Your Name"}),
            'city':forms.TextInput(attrs={"class":"form-control col-6","placeholder":"city"}),
            'state':forms.TextInput(attrs={"class":"form-control col-6","placeholder":"state"}),
            'country':forms.TextInput(attrs={"class":"form-control col-6","placeholder":"country"}),
            'postal_code':forms.TextInput(attrs={"class":"form-control col-6","placeholder":"postal_code"}),
        }
    # address_line_1  = forms.CharField(widget=forms.TextInput(attrs={"class":"form-control col-6","placeholder":"Your Name"}),label='Address')
        