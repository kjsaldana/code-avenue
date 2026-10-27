from django import forms

from .models import Profile

TIMEZONE_CHOICES = [
    ("UTC+1", "UTC+1 España / Francia"),
    ("UTC+0", "UTC+0 España (Canarias) / Reino Unido"),
    ("UTC+2", "UTC+2 Grecia / Rumanía")
]


class ProfileForm(forms.ModelForm):
    email = forms.EmailField(label="email")
    first_name = forms.CharField(label="First name")
    last_name = forms.CharField(label="Last name")

    class Meta:
        model = Profile
        fields = ['photo', 'company', 'profession', 'timezone']
        widgets = {
            'timezone': forms.Select(choices=TIMEZONE_CHOICES)
        }

    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user', None)

        super(ProfileForm, self).__init__(*args, **kwargs)

        if user:
            self.fields['email'].initial = user.email
            self.fields['first_name'].initial = user.first_name
            self.fields['last_name'].initial = user.last_name

    def save(self, commit: bool = True):
        profile = super().save(commit=False)
        user = self.instance.user

        user.email = self.cleaned_data['email']
        user.first_name = self.cleaned_data['first_name']
        user.last_name = self.cleaned_data['last_name']

        if commit:
            user.save()
            profile.save()

        return profile
