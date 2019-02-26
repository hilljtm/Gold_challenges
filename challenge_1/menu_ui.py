
import menu
menu = ()

while True:
    print('Welcome to Komodo Burgers')
    user_input = input('Choose a menu option:\n' +
        '1. Add a option\n' +
        '2. Menu List\n' +
        '3. Update menu Option\n'
        '4. Delete Item\n' +
        '5. Exit')


if user_input == '1':
    meal_number = input('Enter Menu Number: ')
    meal_name = input('Enter Meal Name: ')
    description = input('Enter Description: ')
    ingredients = input('View Ingredients: ')
    price = input('Menu Price: ')

elif user_input == '2':
    menu = menu.get_menu()
    print(menu)

elif user_input == '3':
    menu_to_update = input('Enter menu item to update: ')
    meal_number = input('Enter new Menu: ')
    meal_name = input('Enter new item: ')
    description = input('Enter new description: ')
    ingredients = input('Enter new ingredients: ')
    price = input('Enter new price: ')
    menu.update_menu(meal_number, meal_name, description, ingredients, price)

elif user_input == '4':
    menu_to_del = input('Enter menu item to delete: ')

if menu.delete_menu(menu_to_del) is None:
    print('Item Not Found')
