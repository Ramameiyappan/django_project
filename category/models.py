from django.db import models

class Ledger(models.Model):
    name = models.CharField(max_length=15,null=True, blank=True)
    account_no = models.CharField(max_length=15,null=True, blank=True)
    customer_name = models.CharField(max_length=15,null=True, blank=True)
    amount = models.FloatField(null=True, blank=True)
    commission = models.FloatField(default=0)
    mobile = models.IntegerField(null=True, blank=True)
    topup = models.IntegerField(null=True, blank=True)
    type = models.CharField(max_length=10,null=True, blank=True)
    category = models.CharField(max_length=10,null=True, blank=True)
    balance = models.FloatField()
    connect = models.ForeignKey('Passbook', null=True, blank=True, on_delete=models.SET_NULL)
    created_at = models.DateTimeField(auto_now_add=True)

class Passbook(models.Model):
    bnk_name = [
        ('kvb1','KVB'),
        ('hdfc','HDFC'),
        ('icici','ICICI')
    ]
    transtype = [
        ('deposit','deposit'),
        ('withdraw','withdraw')
    ]

    bank_name = models.CharField(max_length=15,choices=bnk_name)
    transcation_type = models.CharField(max_length=10,choices=transtype)
    purpose = models.CharField(max_length=15)
    deposit = models.FloatField(null=True,blank=True)
    withdraw = models.FloatField(null=True,blank=True)
    balance = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    def save(self,*args,**kwargs):
        if self.transcation_type=='deposit' and self.deposit :
            bal = Passbook.objects.filter(bank_name=self.bank_name).order_by('-id').first()
            if bal:
                self.balance= bal.balance + self.deposit
            else:
                self.balance = self.deposit
        else:
            bal = Passbook.objects.filter(bank_name=self.bank_name).order_by('-id').first().balance - self.withdraw
            if bal<0:
                raise ValueError("Balance is insufficient. Please top up.")
            self.balance = bal
        super().save(*args,**kwargs)