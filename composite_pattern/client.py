from composite_pattern.menu_component import MenuComponent, MenuComposite, MenuItem
from composite_pattern.waitress import Waitress


def main():
    cafe_menu = MenuComposite('Cafe Menu', 'For Dinner')
    diner_menu = MenuComposite('Diner Menu', 'For Lunch')
    all_menus: MenuComponent = MenuComposite('all menus', 'all menus')
    all_menus.add(cafe_menu)
    all_menus.add(diner_menu)
    cafe_menu.add(
        MenuItem(
            "Veggie Burger and Air Fries",
            "Veggie burger on a whole wheat bun, lettuce, tomato, and fries",
            True,
            3.99,
        )
    )
    cafe_menu.add(
        MenuItem(
            "Soup of the day",
            "A cup of the soup of the day, with a side salad",
            False,
            3.69,
        )
    )
    cafe_menu.add(
        MenuItem(
            "Burrito",
            "A large burrito, with whole pinto beans, salsa, guacamole",
            True,
            4.29,
        )
    )
    diner_menu.add(
        MenuItem(
            "Vegetarian BLT",
            "(Fakin') Bacon with lettuce & tomato on whole wheat",
            True,
            2.99,
        )
    )
    diner_menu.add(
        MenuItem(
            "BLT",
            "Bacon with lettuce & tomato on whole wheat",
            False,
            2.99,
        )
    )
    diner_menu.add(
        MenuItem(
            "Soup of the day",
            "Soup of the day, with a side of potato salad",
            False,
            3.29,
        )
    )
    diner_menu.add(
        MenuItem(
            "Hotdog",
            "A hot dog, with sauerkraut, relish, onions, topped with cheese",
            False,
            3.05,
        )
    )
    diner_menu.add(
        MenuItem(
            "Steamed Veggies and Brown Rice",
            "A medly of steamed vegetables over brown rice",
            True,
            3.99,
        )
    )
    diner_menu.add(
        MenuItem(
            "Pasta",
            "Spaghetti with Marinara Sauce, and a slice of sourdough bread",
            True,
            3.89,
        )
    )
    waitress = Waitress(all_menus)
    waitress.print_menu()


if __name__ == "__main__":
    main()