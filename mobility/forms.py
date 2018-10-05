from django import forms

GENDERS = (
        ('m', 'male'),
        ('f', 'female'),
        ('d', 'diverse'),
    )

RADII = (
    (1, '1km'),
    (2, '2km'),
    (5, '5km'),
    (10, '10km'),
)

class SupporterProfileForm(forms.Form):

    profile_image = forms.FileField(required=True, widget=forms.FileInput(attrs={'accept':'image/*'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    gender = forms.ChoiceField(required=True, choices=GENDERS, widget=forms.RadioSelect(attrs={'display': 'inline'}))
    birth_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Birth date'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'About yourself'}))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
    radius = forms.ChoiceField(required=True, choices=RADII, widget=forms.RadioSelect(attrs={'display': 'inline'}))
    #lat = forms.FloatField(required=True)
    #lng = forms.FloatField(required=True, widget=forms.NumberInput(attrs={'type': 'hidden','value': 1}))

class SeniorProfileForm(forms.Form):

    profile_image = forms.FileField(widget=forms.FileInput(attrs={'accept':'image/*'}))
    first_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'First Name'}))
    last_name = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Last Name'}))
    gender = forms.ChoiceField(required=True, choices=GENDERS, widget=forms.RadioSelect(attrs={'display': 'inline'}))
    birth_date = forms.DateField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Birth date'}))
    bio = forms.CharField(widget=forms.Textarea(attrs={'placeholder': 'About yourself'}))
    phone = forms.CharField(required=True, widget=forms.TextInput(attrs={'placeholder': 'Phone number'}))
