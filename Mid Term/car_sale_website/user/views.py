from django.shortcuts import render,redirect
from . import forms
from user.models import History

from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.contrib.auth import authenticate, login, update_session_auth_hash, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required

from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

# Create your views here.


def signup(request):
    if request.method == 'POST':
        signup_form = forms.RegistrationForm(request.POST)
        if signup_form.is_valid():
            signup_form.save()
            messages.success(request, 'Account created successfully')
            return redirect("home")
    else:
        signup_form = forms.RegistrationForm()
    return render(request, 'signup.html', {'form': signup_form})


class UserLoginView(LoginView):
    template_name = 'login.html'
    # success_url = reverse_lazy('profile')

    # uporer success_url diye redirect hocchilo na tai nicher function ta likha

    def get_success_url(self) -> str:
        return reverse_lazy('home')

    def form_valid(self, form):
        messages.success(self.request, 'log in succesfully')
        return super().form_valid(form)

    def form_invalid(self, form):
        messages.success(self.request, 'Can not logged in! User info incorrect')
        return super().form_invalid(form)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     context['type'] = 'Login'
    #     return context

@login_required
def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, data=request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Password Updated successfully')
            update_session_auth_hash(request, form.user)
            return redirect("profile")
    else:
        form = PasswordChangeForm(user=request.user)
    return render(request, 'pass_change.html', {'form': form})


@login_required
def edit_profile(request):
    if request.method == 'POST':
        profile_form = forms.ChangeUserForm(
            request.POST, instance=request.user)
        if profile_form.is_valid():
            profile_form.save()
            messages.success(request, 'Profile Updated successfully')
            return redirect("profile")
    else:
        profile_form = forms.ChangeUserForm(instance=request.user)
    return render(request, 'edit_profile.html', {'form': profile_form})


@login_required
def profile(request):
    data = History.objects.filter(user=request.user)
    return render(request, 'profile.html', {'data': data})
    

@login_required
def user_logout(request):
    logout(request)
    return redirect('login')