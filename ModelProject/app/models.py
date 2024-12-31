from django.db import models

# Create your models here.
class Account(models.Model):
    accountno = models.IntegerField('Account No.')
    name = models.CharField("Name", max_length=50)
    bal = models.FloatField("Balance")


class Loan(models.Model):
    acno = models.ForeignKey(Account, on_delete=models.CASCADE)
    lacno = models.IntegerField("Loan Account No.", unique=True)
    lamt = models.FloatField("Loan Amount")


# from app.models import Account, Loan
# a1 = Account.objects.create(accountno=100, name="Sakeeb", bal=200000)
# a2 = Account.objects.create(accountno=101, name="Rahul", bal=100000)
# a3 = Account.objects.create(accountno=102, name="Snehal", bal=300000)


# l1 = Loan.objects.create(acno=a2, lacno=1001, lamt=2500000)
# l2 = Loan.objects.create(acno=a1, lacno=1002, lamt=3000000)
# l3 = Loan.objects.create(acno=a2, lacno=1003, lamt=2500000)

# Loan.objects.filter(acno__accountno==101)
# Loan.objects.filter(acno__name__icontains='Rahul')

# l1 = Loan.objects.get(id=3)
# l1.acno.name
# l1.acno.bal
# a1 = Account.objects.get(id=2)
# a1.loan_set.all()
# a1.loan_set.filter(lacno=1001)


# Account.objects.all()
# Loan.objects.all()
# a1 = Account.objects.get(id=2)
# a1.delete()
# Account.objects.all()
# Loan.objects.all()