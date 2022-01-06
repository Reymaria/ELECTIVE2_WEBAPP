from django.http import HttpResponse
from django.http.response import Http404
from django.shortcuts import redirect


def unauthorized_user(view_func):
    def wrapper_func (request, *args, **kwargs):
        if request.user.is_authenticated and request.user.is_superuser:
            return redirect ('admin/')
        elif request.user.is_authenticated and request.user.is_active:
            return redirect ('student/')
        else:
            return view_func(request, *args, **kwargs)
    return wrapper_func

# # for student
# def allowed_user1(allowed_role= []):
#     def decorator (view_func):
#         def wrapper_func (request, *args, **kwargs):
#             if request.user.groups.exists():
#                 groups = request.user.groups.all()[1].name
#             if groups in allowed_role:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return redirect ('admin/')
#         return wrapper_func
#     return decorator

# # for staff
# def allowed_user2(allowed_role= []):
#     def decorator (view_func):
#         def wrapper_func (request, *args, **kwargs):
#             if request.user.groups.exist():
#                 groups = request.user.groups.all()[0].name
#             if groups in allowed_role:
#                 return view_func(request, *args, **kwargs)
#             else:
#                 return redirect ('student/')
#         return wrapper_func
#     return decorator
