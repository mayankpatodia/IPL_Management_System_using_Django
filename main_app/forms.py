from django import forms

class EnquiriesForm(forms.Form):
    subject = forms.CharField(label="subject",max_length=100)
    name = forms.CharField(label="name",max_length=100)
    email = forms.CharField(label="email",max_length=100)
    message = forms.CharField(label="message",max_length=100)

# class MessagesForm(forms.Form):
#     name = forms.CharField(label="name",max_length=100)
#     email = forms.CharField(label="email",max_length=100)
#     message = forms.CharField(label="message",max_length=100)
