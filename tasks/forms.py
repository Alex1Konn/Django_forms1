from django import forms

class UserForm(forms.Form):
    #Контактные данные
    first_name = forms.CharField(label='Фамилия',
                                 widget=forms.TextInput(attrs={'placeholder': 'Иванов'})
    )
    name = forms.CharField(label='Имя',
                           widget=forms.TextInput(attrs={'placeholder': 'Иван'})
                           )
    surname = forms.CharField(label='Имя',
                              widget=forms.TextInput(attrs={'placeholder': 'Иванович'}),
                              required=False)

    email = forms.EmailField(label='Email',
                              widget=forms.EmailInput(attrs={'placeholder': 'ivan@example.com'})
                             )
    phone = forms.CharField(label='Телефон',
                             widget=forms.TextInput(attrs={'placeholder': '+79998887799'}),
                            max_length=10)

    #Паспортные данные
    seria = forms.IntegerField(label='Серия паспорта',
                               widget=forms.NumberInput(attrs={'placeholder': '1234'}))
    nomer = forms.IntegerField(label='Номер паспорта',
                               widget=forms.NumberInput(attrs={'placeholder': '456 789'}))

    data_issue = forms.DateField(label='Дата выдачи',
                                 widget=forms.DateInput(attrs={'type': 'date', 'placeholder': 'дд.мм.гггг'}))
    issued_by = forms.CharField(label='Кем выдан',
                                widget=forms.TextInput(attrs={'placeholder': 'Отделом УФМС России...'}))
    code = forms.CharField(label='Код подразделения',
                           widget=forms.TextInput(attrs={'placeholder': '630-040'}))