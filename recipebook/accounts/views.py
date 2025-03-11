from django.contrib.auth.views import LoginView
from .forms import CustomLoginForm


class CustomLoginView(LoginView):
    template_name = 'registration/login.html'
    authentication_form = CustomLoginForm
    redirect_authenticated_user = True

    def get_success_url(self):
        return "/list"

