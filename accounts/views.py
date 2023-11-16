from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views import View
from django.views.generic import CreateView

from accounts.models import Profile
from .forms import UserEditForm, ProfileEditForm


# Create your views here.


class SignUpView(CreateView):
    form_class = UserCreationForm
    template_name = 'accounts/signup.html'
    success_url = reverse_lazy('login')

    def get_queryset(self):
        query = super().get_queryset()
        return query

    def post(self, request, *args, **kwargs):
        form = self.get_form(UserCreationForm)
        if form.is_valid():
            form.save()

            return self.form_valid(form)

    def form_valid(self, form):
        return super().form_valid(form)


@login_required
def dashboard(request):
    user = request.user
    user_profile = Profile.objects.get(user=user)
    context = {
        'user': user,
        'user_profile': user_profile
    }
    return render(request, 'accounts/profile.html', context)


def edit_profile(request):
    if request.POST:
        user_form = UserEditForm(instance=request.user, data=request.POST)
        profile_form = ProfileEditForm(instance=request.user.profile, data=request.POST, files=request.FILES)
        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()
            return render(request, 'accounts/profile.html')
    else:
        user_form = UserEditForm(instance=request.user)
        profile_form = ProfileEditForm(instance=request.user.profile)

    context = {
        'user_form': user_form,
        'profile_form': profile_form,
    }

    return render(request, 'accounts/user_edit.html', context)
