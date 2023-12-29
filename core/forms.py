
from django.contrib.auth.models import User, Group
from django import forms
from django.utils.translation import gettext as _



class ContactForm(forms.Form):
    '''Class used to create contact form '''

    name = forms.CharField(
        required = False,
        widget = forms.widgets.TextInput(
            attrs={
                "placeholder": "Your name",
                "class": "form-control form-control-sm",
                "required": True,
                }
            ),
            label="",
        )
    email = forms.EmailField(
        required = False,
        widget = forms.widgets.EmailInput(
            attrs={
                "placeholder": "Your e-mail",
                "class": "form-control form-control-sm",
                "required": True,
                }
            ),
            label="",
        )

    subject = forms.CharField(
        required=False,
        widget = forms.widgets.TextInput(
            attrs={
                "class": "form-control form-control-sm",
                "placeholder": "Subject",
                "required": True,
                }
            ),
        label="",
    )

    mess = forms.CharField(
        required=False,
        widget = forms.widgets.Textarea(
            attrs={
                 "placeholder": "Enter message here",
                "class": "form-control form-control-sm validate",
                "required": True,
                }
            ),
        label="",
    )
    
