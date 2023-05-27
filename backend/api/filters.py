from enum import Enum

from django.contrib.auth import get_user_model
from django_filters.rest_framework import FilterSet, filters
from rest_framework.filters import SearchFilter

from api.models import Recipe

User = get_user_model()


class UrlQueries(str, Enum):
    # Параметр для поиска ингредиентов по вхождению значения в название
    SEARCH_ING_NAME = 'name'
    # Параметр для поиска объектов в списке "избранное"
    FAVORITE = 'is_favorited'
    # Параметр для поиска объектов в списке "покупки"
    SHOP_CART = 'is_in_shopping_cart'
    # Параметр для поиска объектов по автору
    AUTHOR = 'author'
    # Параметр для поиска объектов по тэгам
    TAGS = 'tags'


class IngredientSearchFilter(SearchFilter):
    search_param = 'name'


class AuthorAndTagFilter(FilterSet):
    tags = filters.BooleanFilter(method='filter_tags')
    author = filters.ModelChoiceFilter(queryset=User.objects.all())
    is_favorited = filters.BooleanFilter(method='filter_is_favorited')
    is_in_shopping_cart = filters.BooleanFilter(
        method='filter_is_in_shopping_cart')

    def filter_tags(self, queryset, name, value):
        if value and not self.request.user.is_anonymous:
            tags = self.request.query_params.getlist(UrlQueries.TAGS.value)
            return queryset.filter(tags__slug__in=tags)
        return queryset

    def filter_is_favorited(self, queryset, name, value):
        if value and not self.request.user.is_anonymous:
            return queryset.filter(favorites__user=self.request.user)
        return queryset

    def filter_is_in_shopping_cart(self, queryset, name, value):
        if value and not self.request.user.is_anonymous:
            return queryset.filter(cart__user=self.request.user)
        return queryset

    class Meta:
        model = Recipe
        fields = ('tags', 'author')
