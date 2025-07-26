from django.shortcuts import render,redirect

from django.views.generic import View

from todoapp.forms import RegistrationForm,LoginForm,TodoForm

from django.contrib.auth.models import User

from django.contrib.auth import authenticate,login,logout

from todoapp.models import Todo


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

                return redirect("todo-create")
            
        return render(request,self.template_name,{"form":form_instance})




class TodoCreateView(View):

    template_name = "todo-create.html"

    form_class = TodoForm


    def get(self,request,*args,**kwargs):

        form_instance = self.form_class()

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        form_data = request.POST

        form_instance = self.form_class(form_data)

        if form_instance.is_valid():

            validated_data = form_instance.cleaned_data

            Todo.objects.create(**validated_data,owner=request.user)

            return redirect("todo-create")
        
        else:

            return render(request,self.template_name,{"form":form_instance})
        

class TodoListView(View):

    template_name="todo_list.html"

    def get(self,request,*args,**kwargs):

        qs=Todo.objects.all()

        return render(request,self.template_name,{"data":qs})
    

class TodoDeleteView(View):

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        Todo.objects.get(id=id).delete()

        return  redirect("todo-list")
    
class TodoUpdateView(View):

    template_name="todo_update.html"

    form_class=TodoForm

    def get(self,request,*args,**kwargs):

        id=kwargs.get("pk")

        todo_object=Todo.objects.get(id=id)

        form_instance=self.form_class(instance=todo_object)

        return render(request,self.template_name,{"form":form_instance})
    
    def post(self,request,*args,**kwargs):

        
        id=kwargs.get("pk")

        form_data=request.POST

        form_instance=self.form_class(form_data)

        if form_instance.is_valid():

            validated_data=form_instance.cleaned_data

            Todo.objects.filter(id=id).update(**validated_data)

            return redirect("todo-list")
        
        else:

            return render(request,self.template_name,{"form":form_instance})


        

    