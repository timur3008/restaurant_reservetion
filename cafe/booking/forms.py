from django import forms

from . import models

class ContactUsForm(forms.ModelForm):
    class Meta:
        model = models.ContactUs
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Jackson'
            }),
            'email': forms.EmailInput(attrs={
                'class': 'form-control',
                'placeholder': 'jackson123@gmail.com'
            }),
            'message': forms.Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'message',
                'rows': '4'
            })
        }

class BookingForm(forms.ModelForm):
    comment = forms.Field(required=False, widget=forms.Textarea(attrs={
        'class': 'form-control',
        'placeholder': 'Comment (Optional)',
        'rows': '4'
    }))
    
    class Meta:
        model = models.Booking
        fields = '__all__'
        widgets = {
            'full_name': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Full Name'
            }),
            'phone': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Phone: 085 456 7890',
                'type': 'tel'
            }),
            'time': forms.TimeInput(attrs={
                'class': 'form-control',
                'type': 'time',
                'value': '18:30'
            }),
            'date': forms.DateInput(attrs={
                'class': 'form-control',
                'type': 'date',
                'placeholder': 'dd.mm.yyyy'
            }),
            'number_of_people': forms.TimeInput(attrs={
                'class': 'form-control',
                'placeholder': 'Number of People',
                'type': 'number'
            })
        }