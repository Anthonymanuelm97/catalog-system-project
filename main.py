business_catalog = [
    {"name": "massage", "price": 500.00, "available": True},
    {"name": "manicure", "price": 200.00, "available": True},
    {"name": "pedicure", "price": 300.00, "available": False},
]


def main():
    while True:
        print("Menu:")
        print("0. Exit")
        print("1. View catalog")

        option = input("Choose an option: ")

        if option == "0":
            print("See you later!")
            break

        if option == "1":
            for product in business_catalog:
                print(f"{product['name']}: ${product['price']}")


if __name__ == "__main__":
    main()
