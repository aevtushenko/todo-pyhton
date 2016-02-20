from django import forms

class NameForm(forms.Form):
    name = forms.CharField(label='Your name', max_length=200)
    email = forms.EmailField(label='Your e-mail', max_length=50)
    hashed_password = forms.CharField(label='Your password', max_length=200)
    hashed_password2 = forms.CharField(label='Confirm password', max_length=200)
    
    
class TaskForm(forms.Form):
    title = forms.CharField(label='Title', max_length=100, initial=' ')
    description = forms.CharField(label='Description', max_length=200, initial=' ')
    collaborator1 = forms.CharField(label='Collaborator', max_length=200, initial=' ')
    collaborator2 = forms.CharField(label='Collaborator', max_length=200, initial=' ')
    collaborator3 = forms.CharField(label='Collaborator', max_length=200, initial=' ')

class LoginForm(forms.Form):
    email = forms.EmailField(label='Your e-mail', max_length=50)
    hashed_password = forms.CharField(label='Your password', max_length=200)
