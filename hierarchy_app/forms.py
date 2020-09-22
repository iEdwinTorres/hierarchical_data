from django import forms
from mptt.forms import TreeNodeChoiceField
from hierarchy_app.models import Tree


class AddTreeForm(forms.Form):
    name = forms.CharField(max_length=200)
    parent = TreeNodeChoiceField(queryset=Tree.objects.all())


class LoginForm(forms.Form):
    username = forms.CharField(max_length=200)
    password = forms.CharField(widget=forms.PasswordInput)
