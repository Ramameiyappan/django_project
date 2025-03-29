from django.shortcuts import render,redirect
from . import forms,models
from django.contrib import messages

def first_category(request):
    return render(request,"first.html")

def electricity_views(request):
    if request.method =='POST':
        ans = forms.Ele_form(request.POST)
        if ans.is_valid():
            instance = ans.save(commit=False)
            last_record = models.Ledger.objects.order_by('-id').first()
            last_balance = float(last_record.balance) if last_record else 0
            if instance.type=='csc':
                bal = last_balance-instance.amount
                if bal < 0:
                    messages.warning(request, 'Balance is insufficient. Please top up.')
                    return redirect('topup_name')
                instance.balance = bal  
            else:
                bank_name = ans.cleaned_data['bank_name']
                instance.balance = last_balance
                bnk_ins = models.Passbook.objects.create(
                    bank_name=bank_name,
                    transcation_type = 'withdraw',
                    purpose=instance.type,
                    withdraw=instance.amount
                )
                bnk_ins.save()
                instance.connect = bnk_ins                
            instance.save()
            return redirect('first_option') 
    else:
        ans = forms.Ele_form()
    return render(request,"electricity.html",{'form':ans})

def recharge_views(request):
    if request.method=='POST':
        ans = forms.Rch_form(request.POST)
        if ans.is_valid():
            instance = ans.save(commit=False)
            last_record = models.Ledger.objects.order_by('-id').first()
            last_balance = float(last_record.balance) if last_record else 0
            if instance.type=='csc':
                bal = last_balance-instance.amount+instance.commission
                if bal < 0:
                    messages.warning(request, 'Balance is insufficient. Please top up.')
                    return redirect('topup_name')
                instance.balance = bal
                instance.mobile = int(instance.account_no)
            else:
                bank_name = ans.cleaned_data['bank_name']
                instance.balance = last_balance
                bnk_ins = models.Passbook.objects.create(
                    bank_name=bank_name,
                    transcation_type = 'withdraw',
                    purpose=instance.name,
                    withdraw=instance.amount
                )
                bnk_ins.save()
                instance.connect = bnk_ins   
            instance.save()
            return redirect('first_option') 
    else:
        ans = forms.Rch_form()
    return render(request,"recharge.html",{'form':ans})

def insurance_views(request):
    if request.method=='POST':
        ans = forms.Ins_form(request.POST)
        if ans.is_valid():
            instance = ans.save(commit=False)
            last_record = models.Ledger.objects.order_by('-id').first()
            last_balance = float(last_record.balance) if last_record else 0
            if instance.type=='csc':
                bal = last_balance-instance.amount+instance.commission
                if bal < 0:
                    messages.warning(request, 'Balance is insufficient. Please top up.')
                    return redirect('topup_name')
                instance.balance = bal  
            else:
                bank_name = ans.cleaned_data['bank_name']
                instance.balance = last_balance
                bnk_ins = models.Passbook.objects.create(
                    bank_name=bank_name,
                    transcation_type = 'withdraw',
                    purpose=instance.name,
                    withdraw=instance.amount
                )
                bnk_ins.save()
                instance.connect = bnk_ins   
            instance.save()
            return redirect('first_option')
    else:
        ans = forms.Ins_form()
    return render(request,"insurance.html",{'form':ans})

def travel_views(request):
    if request.method=='POST':
        ans = forms.Travel_form(request.POST)
        if ans.is_valid():
            instance = ans.save(commit=False)
            last_record = models.Ledger.objects.order_by('-id').first()
            last_balance = float(last_record.balance) if last_record else 0
            if instance.type=='csc':
                bal = last_balance-instance.amount+instance.commission
                if bal < 0:
                    messages.warning(request, 'Balance is insufficient. Please top up.')
                    return redirect('topup_name')
                instance.balance = bal  
            else:
                bank_name = ans.cleaned_data['bank_name']
                instance.balance = last_balance
                bnk_ins = models.Passbook.objects.create(
                    bank_name=bank_name,
                    transcation_type = 'withdraw',
                    purpose=instance.name,
                    withdraw=instance.amount
                )
                bnk_ins.save()
                instance.connect = bnk_ins   
            instance.save()
            return redirect('first_option')
            
    else:
        ans = forms.Travel_form()
    return render(request,"travel.html",{'form':ans})

def pan_views(request):
    if request.method=='POST':
        ans = forms.Pan_form(request.POST)
        if ans.is_valid():
            instance = ans.save(commit=False)
            last_record = models.Ledger.objects.order_by('-id').first()
            last_balance = float(last_record.balance) if last_record else 0
            instance.amount = 107
            if instance.type=='csc':
                if instance.category == 'uti':
                    instance.commission = 9.63
                else:
                    instance.commission = 9.37
                bal = last_balance-instance.amount+instance.commission
                if bal < 0:
                    messages.warning(request, 'Balance is insufficient. Please top up.')
                    return redirect('topup_name')
                instance.balance = bal  
            else:
                bank_name = ans.cleaned_data['bank_name']
                instance.balance = last_balance
                bnk_ins = models.Passbook.objects.create(
                    bank_name=bank_name,
                    transcation_type = instance.category,
                    purpose=instance.name,
                    withdraw=instance.amount
                )
                bnk_ins.save()
                instance.connect = bnk_ins   
            instance.save()
            return redirect('first_option')    
    else:
        ans = forms.Pan_form()
    return render(request,"pan.html",{'form':ans})

def topup_views(request):
    if request.method=='POST':
        ans = forms.Topup_form(request.POST)
        if ans.is_valid():
            instance = ans.save(commit=False)
            last_record = models.Ledger.objects.order_by('-id').first()
            if last_record:
                last_balance = float(last_record.balance)  
            else:
                last_balance = 0
            instance.balance = last_balance+instance.topup 
            bank_name = ans.cleaned_data['bank_name'] 
            bnk_ins = models.Passbook.objects.create(
                bank_name=bank_name,
                transcation_type = 'withdraw',
                purpose=instance.name,
                withdraw=instance.topup
            )
            bnk_ins.save()
            instance.connect = bnk_ins   
            instance.save()
            return redirect('first_option')
    else:
        ans = forms.Topup_form()
    return render(request,"topup.html",{'form':ans})

def esevai_views(request):
    if request.method=='POST':
        ans = forms.Esevai_form(request.POST)
        if ans.is_valid():
            instance = ans.save(commit=False)
            last_record = models.Ledger.objects.order_by('-id').first()
            last_balance = float(last_record.balance) if last_record else 0
            if instance.type=='csc':
                bal = last_balance-instance.amount+instance.commission
                if bal < 0:
                    messages.warning(request, 'Balance is insufficient. Please top up.')
                    return redirect('topup_name')
                instance.balance = bal  
            else:
                bank_name = ans.cleaned_data['bank_name']
                instance.balance = last_balance
                bnk_ins = models.Passbook.objects.create(
                    bank_name=bank_name,
                    transcation_type = 'withdraw',
                    purpose=instance.category,
                    withdraw=instance.amount
                )
                bnk_ins.save()
                instance.connect = bnk_ins   
            instance.save()
            return redirect('first_option')
            
    else:
        ans = forms.Esevai_form()
    return render(request,"esevai.html",{'form':ans})

def enrollment_views(request):
    if request.method=='POST':
        ans = forms.Enrollment_form(request.POST)
        if ans.is_valid():
            instance = ans.save(commit=False)
            last_record = models.Ledger.objects.order_by('-id').first()
            last_balance = float(last_record.balance) if last_record else 0
            instance.balance = last_balance
            bank_name = ans.cleaned_data['bank_name']
            bnk_ins = models.Passbook.objects.create(
                bank_name=bank_name,
                transcation_type = 'withdraw',
                purpose=instance.category,
                withdraw=instance.amount
            )
            bnk_ins.save()
            instance.connect = bnk_ins   
            instance.save()
            return redirect('first_option')
            
    else:
        ans = forms.Enrollment_form()
    return render(request,"enrollment.html",{'form':ans})

def bank_views(request):
    if request.method=='POST':
        ans = forms.Bank_form(request.POST)
        if ans.is_valid():
            instance=ans.save(commit=False)
            last_record = models.Passbook.objects.filter(bank_name=instance.bank_name).order_by('-id').first()
            if last_record:
                last_balance = float(last_record.balance)
            else:
                last_balance = 0
            if instance.transcation_type=='deposit':
                instance.deposit=ans.cleaned_data['deposit'] or 0
                instance.withdraw=None
                instance.balance=last_balance+instance.deposit
            else:
                instance.withdraw=ans.cleaned_data['withdraw'] or 0
                instance.deposit=None
                instance.balance=last_balance-instance.withdraw
            instance.save()
            return redirect('first_option')
            
    else:
        ans = forms.Bank_form()
    return render(request,"bank.html",{'form':ans})