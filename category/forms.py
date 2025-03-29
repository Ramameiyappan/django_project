from django import forms
from django.forms import ModelForm
from . import models

class Ele_form(ModelForm):
    type_choice = [
        ('csc','CSC'),
        ('tneb','TNEB')
    ]

    type = forms.ChoiceField(choices=type_choice, widget=forms.Select(), label='Choose the website')
    bank_name = forms.ChoiceField(choices=models.Passbook.bnk_name, required=False, widget=forms.Select())

    class Meta:
        model = models.Ledger
        fields = ['name','account_no','customer_name','amount','type']
        labels = {
            'name' : 'Enter the category',
            'account_no' : 'Enter the eb number',
            'customer_name': 'Enter the customer name',
            'amount' : 'Enter the eb bill amount',
            'type':'Choose the website'
        }
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly', 'value': 'Electricity'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data.get('type') == 'tneb':
            self.fields['bank_name'].required = True
        else:
            self.fields['bank_name'].widget = forms.HiddenInput()
        
    '''def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name in self.fields:
            self.fields[field_name].required = True
            self.fields[field_name].error_messages = {
                'required': f'{self.fields[field_name].label} is required.'
            }'''

class Rch_form(ModelForm):
    type_choice = [
        ('csc','CSC'),
        ('website','Brand Website')
    ]
    brand_choice = [
        ('jio','JIO'),
        ('airtel','AIRTEL'),
        ('vi','VI'),
        ('bsnl','BSNL'),
        ('dth','DTH')
    ]

    type = forms.ChoiceField(choices=type_choice, widget=forms.Select(), label='Choose the website')
    category = forms.ChoiceField(choices=brand_choice, widget=forms.Select(), label='Choose the brand name')
    bank_name = forms.ChoiceField(choices=models.Passbook.bnk_name, required=False, widget=forms.Select())

    class Meta:
        model = models.Ledger
        fields = ['name','category','account_no','amount','commission','type','mobile']
        exclude = ['mobile']
        labels = {
            'name' : 'Enter the category',
            'account_no' : 'Enter the mobile number',
            'amount' : 'Enter the recharge amount',
            'commission':'Enter the commission amount',
        }
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly', 'value': 'Recharge'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data.get('type') == 'website':
            self.fields['bank_name'].required = True
        else:
            self.fields['bank_name'].widget = forms.HiddenInput()

class Ins_form(ModelForm):
    name_choice = [
        ('insurance','INSURANCE'),
        ('loan','LOAN')
    ]

    type_choice = [
        ('csc','CSC'),
        ('website','Company Website')
    ]
    
    type = forms.ChoiceField(choices=type_choice, widget=forms.Select(), label='Choose the website')
    name = forms.ChoiceField(choices=name_choice, widget=forms.Select(), label='Choose the category')
    bank_name = forms.ChoiceField(choices=models.Passbook.bnk_name, required=False, widget=forms.Select())

    class Meta:
        model = models.Ledger
        fields = ['name','category','account_no','mobile','amount','commission','type']
        labels = {
            'category': 'Enter the company name',
            'account_no' : 'Enter the Insurance/Loan no',
            'mobile':'Enter the customer mobile no',
            'amount' : 'Enter the Insurance/Loan amt',
            'commission':'Enter the Insurance/Loan comm',
        }
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly', 'value': 'Recharge'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data.get('type') == 'website':
            self.fields['bank_name'].required = True
        else:
            self.fields['bank_name'].widget = forms.HiddenInput()
        
class Pan_form(ModelForm):
    type_choice = [
        ('csc','CSC'),
        ('website','PAN Website')
    ]
    website_choice = [
        ('uti','UTI'),
        ('nsdl','NSDL')
    ]

    type = forms.ChoiceField(choices=type_choice, widget=forms.Select(), label='Select source')
    category = forms.ChoiceField(choices=website_choice, widget=forms.Select(), label='Select Pan Type')
    bank_name = forms.ChoiceField(choices=models.Passbook.bnk_name, required=False, widget=forms.Select())

    class Meta:
        model = models.Ledger
        fields = ['name','account_no','customer_name','mobile','type','category','amount','commission']
        exclude = ['amount','commission']
        labels = {
            'account_no' : 'Enter the Application no',
            'customer_name' : 'Enter the customer_name',
            'mobile':'Enter the customer mobile no',    
        }

        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly', 'value': 'Pan'})
        }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data.get('type') == 'website':
            self.fields['bank_name'].required = True
        else:
            self.fields['bank_name'].widget = forms.HiddenInput()    

class Topup_form(ModelForm):
    bank_name = forms.ChoiceField(choices=models.Passbook.bnk_name, required=True, widget=forms.Select())
    class Meta:
        model = models.Ledger
        fields = ['name','topup']
        labels = {
            'topup':'Enter the amount toped up'   
        }
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly', 'value': 'Topup'}),
        }

class Travel_form(ModelForm):
    type_choice = [
        ('csc','CSC'),
        ('website','Website')
    ]
    website_choice = [
        ('train','TRAIN'),
        ('bus','BUS')
    ]

    type = forms.ChoiceField(choices=type_choice, widget=forms.Select(), label='Select source')
    category = forms.ChoiceField(choices=website_choice, widget=forms.Select(), label='Select travel type')
    bank_name = forms.ChoiceField(choices=models.Passbook.bnk_name, required=False, widget=forms.Select())

    class Meta:
        model = models.Ledger
        fields = ['name','category','customer_name','account_no','mobile','amount','commission','type']
        labels = {
            'category': 'Enter the company name',
            'account_no' : 'Enter the Src-Des',
            'customer_name' : 'customer_name',
            'amount' : 'Enter the travel amount',
            'commission':'Enter the commission',
            'mobile':'Enter the customer mobile no',    
        }

        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly', 'value': 'Travel'}),
            'account_no': forms.TextInput(attrs={'placeholder': 'e.g., VM-MS'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data.get('type') == 'website':
            self.fields['bank_name'].required = True
        else:
            self.fields['bank_name'].widget = forms.HiddenInput() 

class Esevai_form(ModelForm):
    type_choice = [
        ('csc','CSC'),
        ('tnega','TNEGA')
    ]
    website_choice = [
        ('community','community'),
        ('nativity','nativity'),
        ('income','income'),
        ('first graduate','first graduate'),
        ('obc','obc'),
        ('old age pension','old age pension'),
        ('widow','widow'),
        ('widow pension','widow pension'),
        ('small farmer','small farmer'),
        ('legal heir','legal heir')
    ]

    type = forms.ChoiceField(choices=type_choice, widget=forms.Select(), label='Select source')
    category = forms.ChoiceField(choices=website_choice, widget=forms.Select(), label='Select certificate name')
    bank_name = forms.ChoiceField(choices=models.Passbook.bnk_name, required=False, widget=forms.Select())
    
    class Meta:
        model = models.Ledger
        fields = ['name','account_no','customer_name','category','mobile','amount','commission','type']
        labels = {
            'account_no':'Enter the certificate no',
            'mobile':'Enter the customer mobile no', 
            'customer_name':'Enter the customer name'   
        }

        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly', 'value': 'Esevai'}),
            'account_no': forms.TextInput(attrs={'placeholder': 'e.g., TN-1234567890'})
        }
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        if self.data.get('type') == 'tnega':
            self.fields['bank_name'].required = True
        else:
            self.fields['bank_name'].widget = forms.HiddenInput()

class Enrollment_form(ModelForm):
    bank_name = forms.ChoiceField(choices=models.Passbook.bnk_name, required=True, widget=forms.Select())

    class Meta:
        model = models.Ledger
        fields = ['name','category','customer_name','account_no','type','mobile','amount']
        labels = {
            'category':'Enter the enrollment name:', 
            'customer_name':'Enter the customer name',  
            'account_no':'Enter the user id',
            'type':'Enter the password',
            'mobile':'Enter the customer mobile no', 
            'amount':'Enter the amount paid',
        }
        widgets = {
            'name': forms.TextInput(attrs={'readonly': 'readonly', 'value': 'Enrollment'})
        }

class Bank_form(ModelForm):
    class Meta:
        model = models.Passbook
        fields = ['bank_name','transcation_type','purpose','deposit','withdraw']
        labels = {
            'purpose':'Enter the purpose',
            'deposit':'Enter the deposit amt',
            'withdraw': 'Enter the withdraw amt'
        }

    def __init__(self,*args,**kwargs):
        super().__init__(*args,**kwargs)
        self.fields['deposit'].required = False
        self.fields['withdraw'].required = False
        self.fields['deposit'].widget = forms.HiddenInput()
        self.fields['withdraw'].widget = forms.HiddenInput()

        if 'transcation_type' in self.data:
            transcation_type = self.data.get('transcation_type')
            if transcation_type=='deposit':
                self.fields['deposit'].widget = forms.NumberInput()
                self.fields['deposit'].required = True
            else:
                self.fields['withdraw'].widget = forms.NumberInput()
                self.fields['withdraw'].required = True