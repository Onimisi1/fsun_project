from django import forms

class FsunForm(forms.Form):
    excel_file = forms.FileField(label='Upload FSUN File')
    user_email = forms.EmailField()
