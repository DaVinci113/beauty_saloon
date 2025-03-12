from django.views.generic import CreateView
from .forms import CustomUserCreate


# Create your views here.
class RegisterView(CreateView):
    form_class = CustomUserCreate
    template_name = 'users/register.html'
    success_url = '/'
