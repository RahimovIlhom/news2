from django.urls import path
from .views import dashboard, SignUpView,edit_profile

urlpatterns = [
    path('profile/', dashboard, name='profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('profile/edit/', edit_profile, name='profile_edit'),
]
