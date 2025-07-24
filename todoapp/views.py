from django.shortcuts import render,redirect

from django.views.generic import View

from todoapp.forms import RegistrationForm,LoginForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout


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

            form_instance.save()

            # validated_data = form_instance.cleaned_data

            # User.objects.create_user(**validated_data)
            

            return redirect("register")
        
        else:

            return render(request,self.template_name,{"form":form_instance})
    

class SignInView(View):

    template_name = "signin.html"

    form_class = LoginForm

    def get(self,request,*args,**kwargs):

        form_instance = self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data = request.POST

        form_instance = self.form_class(form_data)

        if form_instance.is_valid():

            validated_data = form_instance.cleaned_data #{"username":"django","password":"pwd"}

            u_name = validated_data.get("username")

            pwd = validated_data.get("password")

            user_object = authenticate(request,username=u_name,password = pwd)

            if user_object:

                login(request,user_object)

                return redirect("signin")
            
        return render(request,self.template_name,{"form":form_instance})



    