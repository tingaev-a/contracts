from django import forms
from django.forms import ModelForm
from.models import ContractType, Organization, Position, Contract, File



# Форма для ContractType
class ContractTypeForm(ModelForm):
    class Meta:
        model = ContractType
        fields = '__all__'
    fields = ['name', 'description']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'description': forms.Textarea(attrs={'class': 'form-control', 'rows': 4})
    }

# Форма для Organization
class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = [
            'name', 'inn'
        ]
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'inn': forms.TextInput(attrs={'class': 'form-control'}),
        }

class OrganizationUpdateForm(OrganizationForm):
    class Meta(OrganizationForm.Meta):
        exclude = ['registration_date']  # Исключаем поле даты регистрации

# Форма для Position
class PositionForm(ModelForm):
    class Meta:
        model = Position
        fields = '__all__'
    fields = ['name', 'organization']
    widgets = {
        'name': forms.TextInput(attrs={'class': 'form-control'}),
        'organization': forms.Select(attrs={'class': 'form-control'})
    }

# Форма для Contract
class ContractForm(ModelForm):
    class Meta:
        model = Contract
        fields = '__all__'
    fields = ['number', 'date_start', 'date_end', 'contract_type', 'organization']
    widgets = {
        'number': forms.TextInput(attrs={'class': 'form-control'}),
        'date_start': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'date_end': forms.DateInput(attrs={'class': 'form-control', 'type': 'date'}),
        'contract_type': forms.Select(attrs={'class': 'form-control'}),
        'organization': forms.Select(attrs={'class': 'form-control'})
    }

# Форма для File
class FileForm(ModelForm):
    class Meta:
        model = File
        fields = 'file', 'contract'
        widgets = {
            'file': forms.FileInput(attrs={'class': 'form-control-file'}),
            'contract': forms.HiddenInput()
        }

    def clean(self):
        cleaned_data = super(FileForm, self).clean()
        file = cleaned_data.get('file')

        # Проверка размера файла
        if file:
            max_size = 10 * 1024 * 1024  # 10MB
            if file.size > max_size:
                raise forms.ValidationError("Файл слишком большой. Максимальный размер: 10MB")

        return cleaned_data


