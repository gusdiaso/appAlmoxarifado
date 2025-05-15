# form criar almoxarifado

from django import forms
from django.contrib.auth import get_user_model
from .models import Item, Funcionario, AlocaItem, RetiraItem

User = get_user_model()

class ItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'quantidade_total']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade_total': forms.NumberInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'nome': 'Nome do Item',
            'quantidade_total': 'Quantidade Total',
        }

class EditItemForm(forms.ModelForm):
    class Meta:
        model = Item
        fields = ['nome', 'quantidade_total']
        widgets = {
            'nome': forms.TextInput(attrs={'class': 'form-control'}),
            'quantidade_total': forms.TextInput(attrs={'class': 'form-control', 'readonly': 'readonly'})
        }
        labels = {
            'nome': 'Nome do Item',
            'quantidade_total': 'Quantidade Total',
        }


class AlocaItemForm(forms.ModelForm):
    funcionario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Funcionário'
    )
    class Meta:
        model = AlocaItem
        fields = ['funcionario', 'item', 'quantidade', 'descricao']
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'item': 'Item',
            'quantidade': 'Quantidade',
            'descricao': 'Descrição'
        }

class RetiraItemForm(forms.ModelForm):
    funcionario = forms.ModelChoiceField(
        queryset=User.objects.all(),
        widget=forms.Select(attrs={'class': 'form-control'}),
        label='Funcionário'
    )
    class Meta:
        model = RetiraItem
        fields = ['funcionario', 'item', 'quantidade', 'descricao']
        widgets = {
            'item': forms.Select(attrs={'class': 'form-control'}),
            'quantidade': forms.NumberInput(attrs={'class': 'form-control'}),
            'descricao': forms.TextInput(attrs={'class': 'form-control'}),
        }
        labels = {
            'item': 'Item',
            'quantidade': 'Quantidade',
            'descricao': 'Descrição'
        }