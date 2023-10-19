from django import forms
from .models import UserProfile, Departments, Courses, Materials  # Import your models

GENDER_CHOICES = [
    ('male', 'Male'),
    ('female', 'Female'),
]

PURPOSE_CHOICES = [
    ('enquiry', 'For Enquiry'),
    ('order', 'Place Order'),
    ('return', 'Return'),
]


class UserForm(forms.Form):
    name = forms.CharField(max_length=100)
    dob = forms.DateField(widget=forms.TextInput(attrs={'type': 'date'}))
    age = forms.IntegerField()
    gender = forms.ChoiceField(widget=forms.RadioSelect, choices=GENDER_CHOICES)
    phone_number = forms.CharField(max_length=15)
    email = forms.EmailField()
    address = forms.CharField(widget=forms.Textarea)
    department = forms.ModelChoiceField(queryset=Departments.objects.all())
    purpose = forms.ChoiceField(choices=PURPOSE_CHOICES)
    materials_provided = forms.ModelMultipleChoiceField(
        queryset=Materials.objects.all(),
        widget=forms.CheckboxSelectMultiple
    )

# class UserForm(forms.ModelForm):
#     class Meta:
#         model = UserProfile
#         fields = ['name', 'dob', 'age', 'gender', 'phone_number', 'email', 'address', 'department', 'course', 'purpose',
#                   'materials_provided']
