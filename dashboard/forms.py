from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.core.files import File
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm


class UploadFileForm(forms.Form):
    # title = forms.CharField(max_length=50)
    file = forms.FileField()


NGO_CHOICES = (
    ('one', 'Control of corruption'),
    ('two', 'Political Stability'),
    ('three', 'Inflation Rate'),
    ('four', 'Gdp Growth'),
    ('two', 'Ease of Doing Business'),
    ('three', 'Unemployment Rate',),
    ('one', 'Individuals using the Internet'),
)
criteria = ['Control of corruption', 'Political Stability', 'Inflation Rate', 'Gdp Growth',
            'Ease of Doing Business', 'Unemployment Rate',
            'Individuals using the Internet']


class CriteriaForm(forms.Form):
    criteria = forms.MultipleChoiceField(widget=forms.CheckboxSelectMultiple,
                                         choices=NGO_CHOICES)
    w1 = forms.FloatField(min_value=0, max_value=100)
    w2 = forms.FloatField(min_value=0, max_value=100)
    w3 = forms.FloatField(min_value=0, max_value=100)
    w4 = forms.FloatField(min_value=0, max_value=100)
    w5 = forms.FloatField(min_value=0, max_value=100)
    w6 = forms.FloatField(min_value=0, max_value=100)
    w7 = forms.FloatField(min_value=0, max_value=100)

    def total_weights(self):
        return sum([self.w1, self.w2, self.w3, self.w4, self.w5, self.w6, self.w7])


class DownloadFileForm(forms.Form):
    file = File(open('template.csv', 'w+'))


class UserRegisterForm(UserCreationForm):
    email = forms.EmailField()

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']
