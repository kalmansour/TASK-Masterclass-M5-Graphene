from graphene_django import DjangoObjectType

from food.models import Cuisine, Ingredient, Recipe

class IngredientType(DjangoObjectType):
    class Meta:
        model = Ingredient
        fields = ("id","name", "origin")

class CuisineType(DjangoObjectType):
    class Meta:
        model = Cuisine
        fields = ("id","name")

class RecipeType(DjangoObjectType):
    class Meta:
        model = Recipe
        fields = ("id","name","steps", "ingredients", "cuisine")