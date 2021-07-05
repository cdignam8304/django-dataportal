from django.shortcuts import render
from django.views import View
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.shortcuts import redirect, get_object_or_404
from .models import App, AppCategory

# Create your views here.

# class Homepage(LoginRequiredMixin, View): # NEED TO IMPLEMENT AUTHENTICATION !!!
class Homepage(View):
	login_url = "/login/"
	redirect_field_name = "redirect_to"
	title = "Data Portal Home"
	apps = App.objects.all() #.values_list('app_name', 'app_category')
	app_categories = AppCategory.objects.all()
	
	def get(self, request):
		context = {}
		context["title"] = self.title
		context["apps"] = self.apps
		context["app_categories"] = self.app_categories
		
		return render(
			request=request,
			template_name="main/homepage.html",
			context=context,
		)


class CustomDashboard(View):
	title = "Create Custom Dashboard"
	apps = App.objects.all() #.values_list('app_name', 'app_category')
	app_categories = AppCategory.objects.all()
	
	def get(self, request):
		context = {}
		context["title"] = self.title
		context["apps"] = self.apps
		context["app_categories"] = self.app_categories
		
		return render(
			request=request,
			template_name="main/custom_dashboard.html",
			context=context,
		)


class Test(View):
	title = "Test View"
	
	def get(self, request):
		context = {}
		context["title"] = self.title
		
		return render(
			request=request,
			template_name="main/test.html",
			context=context,
		)