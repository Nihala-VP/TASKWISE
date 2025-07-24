from django.shortcuts import render,redirect

from django.views.generic import View

from todoapp.forms import RegistrationForm

from django.contrib.auth.models import User


class SignUpView(View):

    template_name = "register.html"

    form_class = RegistrationForm

    def get(self,request,*args,**kwargs):

        form_instance = self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data = request.POST

        form_instance = self.form_class(form_data)

        if form_instance.is_valid():

            validated_data = form_instance.cleaned_data

            User.objects.create_user(**validated_data)
            

            return redirect("register")
        
        else:

            return render(request,self.template_name,{"form":form_instance})