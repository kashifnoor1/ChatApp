from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages

def chatPage(request):
    if not request.user.is_authenticated:
        return redirect("login-user")
    return render(request, "chat/chatPage.html")

def registerPage(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")

        if password != confirm_password:
            messages.error(request, "Passwords do not match!")
            return redirect("register-user")

        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already taken!")
            return redirect("register-user")

        User.objects.create_user(username=username, password=password)
        messages.success(request, "Account created successfully! You can now log in.")
        return redirect("login-user")
    return render(request, "chat/RegisterPage.html")



# from django.shortcuts import render, redirect
# from django.contrib.auth.models import User
# from django.contrib import messages

# def chatPage(request, *args, **kwargs):
#     if not request.user.is_authenticated:
#         return redirect("login-user")
#     context = {}
#     return render(request, "chat/chatPage.html", context)

# def registerPage(request):
#     if request.method == "POST":
#         username = request.POST.get("username")
#         password = request.POST.get("password")
#         confirm_password = request.POST.get("confirm_password")

#         if password != confirm_password:
#             messages.error(request, "Passwords do not match!")
#             return redirect("register-user")

#         if User.objects.filter(username=username).exists():
#             messages.error(request, "Username already taken!")
#             return redirect("register-user")

#         # Create the user
#         User.objects.create_user(username=username, password=password)
#         messages.success(request, "Account created successfully! You can now log in.")
#         return redirect("login-user")

#     return render(request, "chat/RegisterPage.html")







# from django.shortcuts import render, redirect


# def chatPage(request, *args, **kwargs):
#     if not request.user.is_authenticated:
#         return redirect("login-user")
#     context = {}
#     return render(request, "chat/chatPage.html", context)

