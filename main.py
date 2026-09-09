business_catalog = [
    {"name": "massage", "price": 500.00, "available": True},
    {"name": "manicure", "price": 200.00, "available": True},
    {"name": "pedicure", "price": 300.00, "available": False},
]


def search_product(catalog, name_searched):
    for product in catalog:
        if product["name"] == name_searched:
            return product
    return None


def main():
    while True:
        print("Menu:")
        print("0. Exit")
        print("1. View catalog")
        print("2. Search a product")

        option = input("Choose an option: ")

        if option == "0":
            print("See you later!")
            break

        if option == "1":
            for product in business_catalog:
                print(f"{product['name']}: ${product['price']}")

        if option == "2":
            name_searched = input("Enter the product name: ")
            product = search_product(business_catalog, name_searched)

            if product is not None:
                print(product)
            else:
                print("product not found")


if __name__ == "__main__":
    main()
