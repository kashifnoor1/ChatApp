from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from . import views

urlpatterns = [
    path("", views.chatPage, name="chat-page"),
    path("auth/register/", views.registerPage, name="register-user"),
    path("auth/login/", LoginView.as_view(template_name="chat/LoginPage.html"), name="login-user"),
    path("auth/logout/", LogoutView.as_view(), name="logout-user"),
]






# from django.urls import path, include
# from chat import views as chat_views
# from django.contrib.auth.views import LoginView, LogoutView


# urlpatterns = [
#     path("", chat_views.chatPage, name="chat-page"),

#     # login-section
#     path("auth/login/", LoginView.as_view
#          (template_name="chat/LoginPage.html"), name="login-user"),
#     path("auth/logout/", LogoutView.as_view(), name="logout-user"),
# ]