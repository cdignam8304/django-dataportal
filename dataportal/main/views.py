from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404

# Create your views here.

# class Homepage(LoginRequiredMixin, View): # NEED TO IMPLEMENT AUTHENTICATION !!!
class Homepage(View):
    login_url = "/login/"
    redirect_field_name = "redirect_to"
    title = "Data Portal Home"
    portal_apps = [
            "KPI1",
            "KPI2",
            "KPI3",
            "App1",
            "App1",
            "App1",
            ]
    
    def get(self, request):
        context = {}
        context["title"] = self.title
        context["portal_apps"] = self.portal_apps
        return render(
            request=request,
            template_name="main/homepage.html",
            context=context,
            )