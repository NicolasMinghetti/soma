from django import forms

class NameForm(forms.Form):
    choix = forms.CharField(label='choix', max_length=5)
    choix1= forms.CharField(label='choix1', max_length=30)
    choix2= forms.CharField(label='choix2', max_length=30)
    choix3= forms.CharField(label='choix3', max_length=30)
