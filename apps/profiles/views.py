from django.contrib import messages
from django.contrib.auth.mixins import LoginRequiredMixin
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic.edit import UpdateView
from .forms import ProfileForm
from .models import Profile


def profile(request):
    return render(request, "profiles/profile.html")


class ProfileUpdateView(LoginRequiredMixin, UpdateView):
    model = Profile
    form_class = ProfileForm
    template_name = 'profiles/profile.html'
    success_url = reverse_lazy('profile')

    def get_object(self, queryset=None):
        return self.request.user.profile

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        profile = self.get_object()
        context[
            'profile_picture'] = profile.photo.url if profile.photo else "https://geekflare.com/es/wp-content/plugins/wp-user-avatars/wp-user-avatars/assets/images/mystery.jpg"
        return context

    def form_valid(self, form):
        messages.success(self.request, 'Tu perfil se ha actualizado correctamente.')
        return super().form_valid(form)
1