from django.shortcuts import redirect



def Authenticated(view_func):
    def wrapper_func(request,*args,**kwargs):
        if request.user.is_authenticated:
            return redirect('store')
        else:

             return view_func(request,*args,**kwargs)
    return wrapper_func 