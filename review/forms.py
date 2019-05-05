from django import forms
from .models import Review

RatingChoices = [
    ('1', '1'),
    ('2', '2'),
    ('3', '3'),
    ('4', '4'),
    ('5', '5'),
]

class ReviewForm(forms.ModelForm):
    name = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': "Name of the customer",
            "class": "input-field"
        }
    ), label='Name')

    emailID = forms.EmailField(widget=forms.TextInput(
        attrs={
            'placeholder': "Email of the customer",
            "class": "input-field"
        }
    ), label='Email')

    mobileNumber = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': "Contact Number of the customer",
            "class": "input-field"
        }
    ), label='Mobile Number')

    rating = forms.ChoiceField(choices=RatingChoices, label="Rating", initial='', widget=forms.Select(
        attrs={
            "class": "dropdown-button btn-flat",
            "style": "color:black"
        }
    ), required=True)

    review = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': "Write a review",
            "class": "input-field"
        }
    ), label='Review')

    city = forms.CharField(widget=forms.TextInput(
        attrs={
            'placeholder': "City of the customer",
            "class": "input-field"
        }
    ), label='City')

    class Meta:
        model = Review
        fields = ("name", "emailID", "mobileNumber", "city", "rating", "review")
