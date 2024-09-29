from datetime import date
import datetime
from django import forms
from django.core.exceptions import ValidationError
from .widgets import CustomClearableFileInput
from .models import Product, Category, WorkoutProgram


class DateInput(forms.DateInput):
    input_type = 'date'


class ProductForm(forms.ModelForm):
    """ product form """

    class Meta:
        model = Product
        fields = '__all__'

    image = forms.ImageField(label='Image',
                             required=False,
                             widget=CustomClearableFileInput
                             )

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        categories = Category.objects.all()
        friendly_names = [(c.id, c.get_friendly_name()) for c in categories]

        self.fields['category'].choices = friendly_names
        for field_name, field in self.fields.items():
            field.widget.attrs['class'] = 'border-black rounded-0'


class WorkoutProgramForm(forms.ModelForm):
    """ workout program form """

    today = date.today()
    delta = datetime.timedelta(days=84)  # 12 x 7

    start_date = forms.DateField(initial=today, required=True,
                                 widget=forms.DateInput(attrs={'type': 'date'})
                                 )
    end_date = forms.DateField(initial=(today + delta), required=True,
                               widget=forms.DateInput(attrs={'type': 'date'})
                               )

    class Meta:
        model = WorkoutProgram
        fields = ['trainer', 'start_date', 'number_weeks',
                  'end_date', 'class_size'
                  ]

        widgets = {
            'start_date': DateInput(),
            'end_date': DateInput(),
        }

    def clean(self):
        cleaned_data = super().clean()
        start_date = cleaned_data.get('start_date')
        end_date = cleaned_data.get('end_date')

        if start_date >= end_date:
            raise ValidationError(
                 "Start date must be less than end date!!.")

        return self.cleaned_data

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        for field_name, field in self.fields.items():
            if filed != 'image':
                field.widget.attrs['class'] = 'border-black rounded-0'
