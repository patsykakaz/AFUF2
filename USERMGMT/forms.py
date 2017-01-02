#-*- coding: utf-8 -*-

from __future__ import unicode_literals
import hashlib
from django import forms
from django.conf import settings
from django.core.mail import send_mail,EmailMultiAlternatives
from django.forms import ModelForm
from django.contrib.admin.widgets import AdminDateWidget 

from models import *

class DateInput(forms.DateInput):
    input_type = 'date'

class NewUserForm(ModelForm):
    class Meta:
        model = Profile
        # fields = ['date_naissance']
        exclude = ['user', 'choix_adhesion']
        widgets = {
            # 'date_naissance': DateInput(),
            'diplome_master_2': forms.RadioSelect(),
            'diplome_DESC_andrologie': forms.RadioSelect(),
            'diplome_DESC_oncologie_1': forms.RadioSelect(),
            'diplome_DESC_oncologie_2': forms.RadioSelect(),
            'diplome_autre': forms.Textarea(attrs={'rows':2}),
            'statut_autre': forms.Textarea(attrs={'rows':4}),
        }

    def clean(self):
        if len(User.objects.filter(email=self.cleaned_data.get('email'))):
            self.add_error('email',"Adresse email déjà présente en base de données.")
            raise forms.ValidationError("Adresse mail invalide")
        # try:
        subject= "Inscription sur le site de l'AFUF"
        from_email = settings.NO_REPLY
        to = self.cleaned_data.get('email')
        username = self.cleaned_data.get('prenom')+'_'+self.cleaned_data.get('nom')
        # building password as it'll be made in view
        passwordBase = self.cleaned_data.get('email')+self.cleaned_data.get('nom')
        hash_object = hashlib.sha256(passwordBase.encode('utf8'))
        password = hash_object.hexdigest()
        password = str(password)[:8]
        print "password in form is : %s" % password
        text_content = u"Merci de vous être inscrit sur notre site www.afuf.fr, une fois que vous aurez réglé votre adhésion pour 2017. \nVotre login : "+username+" \nVotre mot de passe : "+password
        html_content = u"<p><b>Merci de vous être inscrit sur notre site www.afuf.fr</b>, une fois que vous aurez réglé votre adhésion pour 2017. <br /> Votre login : "+username+" <br />Votre mot de passe : "+password+"</p>"
        msg = EmailMultiAlternatives(subject, text_content, from_email, [to])
        msg.attach_alternative(html_content, "text/html")
        print "about to send mail"
        msg.send()
        print "mail shoud be sent"
        # except:
        #     self.add_error('email', '')
        #     raise forms.ValidationError("L'adresse mail soumise semble invalide")
        return self.cleaned_data



class LoginForm(forms.Form):
    username = forms.CharField(label='Adresse mail', widget=forms.EmailInput)
    password = forms.CharField(label='mot de passe', widget=forms.PasswordInput)

    # def clean(self):
    #     email = self.cleaned_data.get('email')
    #     password = self.cleaned_data.get('password')
    #     if not len(User.objects.filter(email=email)):
    #         msg=''
    #         self.add_error('email', msg)
    #         # self.add_error('password', msg)
    #         raise forms.ValidationError("Adresse email inexistante")
    #     return self.cleaned_data

class UserForm(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'password',]
