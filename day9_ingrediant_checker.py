recipe_ingredients = {"flour", "eggs", "milk", "butter", "sugar"}

available_ingredients = set()

while True:
    item = input ("Available Ingredient? ")

    if not item:
        break
    else:
        available_ingredients.add(item)

missing_ingredients = recipe_ingredients.difference(available_ingredients)
extra_ingredients = available_ingredients.difference(recipe_ingredients)

print(missing_ingredients)
print(extra_ingredients)