from django import forms

from visha_app1.models import PortfolioContact





class PortfolioContactform(forms.ModelForm):

    class Meta:

        model = PortfolioContact

        fields = '__all__'







