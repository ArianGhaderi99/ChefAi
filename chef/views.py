import json

from django.http import JsonResponse
from django.shortcuts import render

from chef.api_service import (
    generate_recipe_ai
)


def chef_ai_page(request):

    return render(
        request,
        "chef/chef-ai.html"
    )


def generate_recipe(request):

    if request.method != "POST":

        return JsonResponse(
            {"error": "POST required"},
            status=400
        )

    data = json.loads(
        request.body
    )

    ingredients = data.get(
        "ingredients",
        ""
    )

    answer = generate_recipe_ai(
        ingredients
    )

    return JsonResponse({
        "answer": answer
    })