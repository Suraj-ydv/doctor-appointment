from adminsapp.models import Admins, Add_news
from django import forms


class AdminsForm(forms.ModelForm):
    class Meta:
        model = Admins
        fields = "__all__"


class Add_newsForm(forms.ModelForm):
    class Meta:
        model = Add_news
        fields = ['title','description','image']
