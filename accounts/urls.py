from django.urls import path
from accounts.views import SignInView, SignUpView, sign_out, ProfileView

urlpatterns = [
    path('signin', SignInView.as_view(), name='signin'),
    path('signup', SignUpView.as_view(), name='signup'),
    path('signout', sign_out, name='signout'),
    path('profile', ProfileView.as_view(), name='profile'),
]