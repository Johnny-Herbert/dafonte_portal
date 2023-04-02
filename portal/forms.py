# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django import forms
from django.db.models import Q
from .models import Contact, OpportunityRole


class ContactForm(forms.ModelForm):
    name = forms.CharField(label='Nome', max_length=100, required=False)
    email = forms.CharField(label='Email', max_length=70, required=False)
    telefone = forms.CharField(label='Telefone', max_length=20, required=False)
    message = forms.CharField(label="Mensagem", required=False)

    class Meta:
        model = Contact
        fields = ('name', 'email', 'telefone', 'message')


class OpportunityRoleForm(forms.ModelForm):

    class Meta:
        model = OpportunityRole
        fields = ('id', 'name', 'role_type')

    def clean(self):
        cleaned_data = super().clean()
        name = cleaned_data.get('name', '')
        if not name:
            raise forms.ValidationError(f"O cargo {name} já existe")

        name = name.strip()
        role_type = name.upper()
        cleaned_data['role_type'] = role_type
        exists = OpportunityRole.objects.filter(
            Q(name=name) | Q(role_type=role_type)
        ).exists()
        if exists:
            raise forms.ValidationError(f"O cargo {name} já existe")

        return cleaned_data
