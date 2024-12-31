from django import forms

class RegisterForm(forms.Form):
    cust_name = forms.CharField(label="Customer Name :", max_length=10)
    cust_contact = forms.IntegerField(label="Customer Contact :")

    cust_name.widget.attrs.update({'class':'form-control'})
    cust_contact.widget.attrs.update({'class':'form-control'})
