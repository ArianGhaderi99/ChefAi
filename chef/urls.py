from django.urls import path
from .views import chef_ai_page, generate_recipe

app_name = "chef"

urlpatterns = [
    path('', chef_ai_page, name="ai"),
    path("api/",generate_recipe,name="generate_recipe"),
]