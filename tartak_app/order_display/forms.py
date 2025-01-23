from django import forms
from .models import Element, Order, Client
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit, Row, Column, Field, Div
from searchableselect.widgets import SearchableSelect

class ElementForm(forms.ModelForm):
    element_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model=Element
        fields = ['element_form','name', 'width', 'height', 'length','count', 'description','unit']
        widgets = {
            'unit': forms.RadioSelect(),
        }
    unit = forms.ChoiceField(choices=Element.Units),
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.layout = Layout(
            "element_form",
            'name',
            Row(
                'unit',
                Field('count', id="amount"),
                ),
            Row(
                Column('width', css_class='form-group col-md-4 mb-0'),
                Column('height', css_class='form-group col-md-4 mb-0'),
                Column('length', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
            Submit('submit', 'Zatwierdź')
        )
    
class OrderForm(forms.ModelForm):
    order_form = forms.BooleanField(widget=forms.HiddenInput, initial=True)
    class Meta:
        model=Order
        fields = ['order_form','status','due','adres', 'workers']
        
        widgets = {
            'workers': forms.CheckboxSelectMultiple,
            'due':forms.DateInput(attrs={'type': 'date'}),
        }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Div(css_id = "client_searches_div"),
            'order_form',
            'adres',
            Field('workers',id="workers"),
            Row(
                Column('status', css_class='form-group col-md-4 mb-0'),
                Column('due', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
        )
        
        
class ClientForm(forms.ModelForm):
    class Meta:
        model=Client
        fields = ['first_name','last_name','phone_number']
        widgets = {
                'first_name':forms.TextInput(attrs={'css_id': 'client_first_name'}),
                'last_name':forms.TextInput(attrs={'id': 'client_last_name'}),
                'phone_number':forms.TextInput(attrs={'id': 'client_phone_number'}),
            }
        
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_tag = False
        self.helper.layout = Layout(
            Row(
                Column('first_name', css_class='form-group col-md-4 mb-0'),
                Column('last_name', css_class='form-group col-md-4 mb-0'),
                Column('phone_number', css_class='form-group col-md-4 mb-0'),
                css_class='form-row'
            ),
        )