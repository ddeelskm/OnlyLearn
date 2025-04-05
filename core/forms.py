from django import forms

from core.models import BannerText


class BannerTextForm(forms.ModelForm):
    class Meta:
        model = BannerText
        fields = ['title', 'published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }
