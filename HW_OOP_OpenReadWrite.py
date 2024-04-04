# import os.path
# import os

from pprint import pprint

# задача №1 - создание словаря Книга рецептов, в котором ключи - название рецепта,
# а значение - список ингредиентов в виде словаря (название ингредиента, мера измерения и количество)
with open('recipes.txt', 'r', encoding='utf-8') as file_recipes:
    recipes_book = {}
    for line in file_recipes:
        recipe_name = line.strip()
        ingredients_count = int(file_recipes.readline())
        ingredients = []
        for ingr in range(ingredients_count):
            ingredient = file_recipes.readline().strip()
            ingredient_name, quantity, measure = ingredient.split(' | ')
            ingredients.append({
                'ingredient_name': ingredient_name,
                'quantity': quantity,
                'measure': measure
            })
        recipes_book[recipe_name] = ingredients
        file_recipes.readline()
pprint(recipes_book)

# функия для подсчета количества ингредиентов по рецептам для покупки
def get_shop_list_by_dishes(dishes, person_count):
    shop_dict = {}
    ingred_shop = {}
    for dish in dishes:
        if dish in recipes_book:
            for ingr in recipes_book[dish]:
                product = ingr['ingredient_name']
                measure = ingr['measure']
                quantity = int(ingr['quantity']) * person_count
                ingred_shop = {'measure': measure, 'quantity': quantity}
                if product in shop_dict:
                    shop_dict[product]['quantity'] += quantity
                else:
                    shop_dict[product] = {'measure': measure, 'quantity': quantity}
        else:
            return "Такого блюда нет в списке"
    return shop_dict
pprint(get_shop_list_by_dishes(['Омлет', 'Омлет'], 2))

