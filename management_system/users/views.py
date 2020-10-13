from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.http import Http404
from .forms import RegisterForm, UserUpdateForm, ProfileUpdateForm
from .models import Profile


class SignUpView(generic.CreateView):
    form_class = RegisterForm
    success_url = reverse_lazy('info')
    template_name = 'registration/signup.html'

    def form_valid(self, form):
        view = super().form_valid(form)
        username, password = form.cleaned_data.get('username'), form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        staff = Profile(user=user)
        staff.save()
        login(self.request, user)
        return view


@login_required
def update_profile(request):
    if request.method == 'POST':
        user_form = UserUpdateForm(instance=request.user, data=request.POST)
        profile_form = ProfileUpdateForm(instance=request.user.profile, data=request.POST, files=request.FILES)

        if user_form.is_valid() and profile_form.is_valid():
            user_form.save()
            profile_form.save()

    else:
        user_form = UserUpdateForm(instance=request.user)
        profile_form = ProfileUpdateForm(instance=request.user.profile)

    return render(request, 'registration/update.html', {'user_form': user_form, 'profile_form': profile_form})

# class UpdateUserView(generic.UpdateView):
#     model = Staff
#     template_name = 'registration/update.html'
#     fields = ['username', 'first_name', 'last_name', 'email']
#     success_url = 'registration/login.html'
#
#     def get_object(self):
#         user = self.request.user
#         staff = Staff.objects.get(user = user)
#         if not staff:
#             raise Http404
#         return staff
