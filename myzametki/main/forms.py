from .models import Note
from django import forms
from django.forms import ModelForm, TextInput, Textarea, DateTimeInput
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.models import User

class NoteForm(ModelForm):
    class Meta:
        model = Note
        fields = ['title', 'text', 'date']

        widgets = {
            "title": TextInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Тема заметки'
            }),
            "text": Textarea(attrs={
                'class': 'form-control',
                'placeholder': 'Текст заметки'
            }),
            "date": DateTimeInput(attrs={
                'class': 'form-control',
                'placeholder' : 'Дата добавления'
            })
        }

class AuthUserForm(AuthenticationForm, ModelForm):
    class Meta:
        model = User
        fields = ['username', 'password']


class RegisterUserForm(ModelForm):
    password1 = forms.CharField(label='Введите пароль', widget=forms.PasswordInput)
    password2 = forms.CharField(label='Повторите пароль', widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username']

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError("Пароли не совпадают")
        return password2

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
            if hasattr(self, "save_m2m"):
                self.save_m2m()
        return user