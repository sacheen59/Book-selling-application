from django.shortcuts import redirect



# give access to admin page if request comes from admin
# if request is from normal user redirect to user page

def admin_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_staff:
            return view_func(request, *args, **kwargs)
        else:
            return redirect('/')
    return wrapper_func

# give access to user pages if request comes from user
# if request is from admin redirect to admin_dashboard

def user_only(view_func):
    def wrapper_func(request, *args, **kwargs):
        if request.user.is_staff:
            return redirect('/admin/dashboard')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func