from iterator_pattern.menus import CafeMenu, DinerMenu, PancakeHouseMenu
from iterator_pattern.waitress import Waitress


def main():
    cafe_menu = CafeMenu()
    diner_menu = DinerMenu()
    pancake_house_menu = PancakeHouseMenu()
    menus = [cafe_menu, diner_menu, pancake_house_menu]
    waitress = Waitress(menus)
    waitress.print_menu()
    print("\nCustomer asks, is the Hotdog vegetarian?")
    print("Waitress says: ", end="")
    if waitress.is_item_vegetarian("Hotdog"):
        print("Yes")
    else:
        print("No")

if __name__ == "__main__":
    main()