from django import forms

from core.models import BannerText, CustomerReviews


class BannerTextForm(forms.ModelForm):
    class Meta:
        model = BannerText
        fields = ['title', 'published']
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'})
        }


class CustomerReviewsForm(forms.ModelForm):
    class Meta:
        model = CustomerReviews
        fields = ['name', 'reviews', 'image', 'published']
        labels = {
            'image': 'Аватарка отзыва:'
        }

        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'reviews': forms.Textarea(attrs={'class': 'form-control'}),
            'image': forms.FileInput(attrs={'class': 'form-control'}),
            'published': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
