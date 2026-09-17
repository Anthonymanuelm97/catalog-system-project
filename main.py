business_catalog = [
    {"name": "massage", "price": 500.00, "available": True},
    {"name": "manicure", "price": 200.00, "available": True},
    {"name": "pedicure", "price": 300.00, "available": False},
]


class Business:
    def __init__(self, catalog):
        self.catalog = catalog

    def view_catalog(self):
        for product in self.catalog:
            print(f"{product['name']}: ${product['price']}")

    def search_product(self, name_searched):
        for product in self.catalog:
            if product["name"].lower() == name_searched.lower():
                return product
        return None

    def add_product(self, name, price, available):
        try:
            price_number = float(price)
        except ValueError:
            print("The price must be a number. Product not added")
            return None

        new_product = {
            "name": name,
            "price": price_number,
            "available": available,
        }
        self.catalog.append(new_product)
        return new_product

    def available_product(self):
        return [product for product in self.catalog if product["available"]]


def available_product(catalog, available=None):
    if available is not None:
        available_products = []
        for product in catalog:
            if product["available"] == available:
                available_products.append(product)
        return available_products


def main():
    while True:
        print("Menu:")
        print("0. Exit")
        print("1. View catalog")
        print("2. Search a product")
        print("3. Add a new product")
        print("4. View available products")

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

        if option == "3":
            name = input("Enter the product name: ")
            price = float(input("Enter the product price: "))
            available = input("Is it available? (True/False): ") == "True"

            new_product = add_product(business_catalog, name, price, available)
            print(f"Product added: {new_product}")

        if option == "4":
            available_catalog = available_products(business_catalog)
            for product in available_catalog:
                print(f"{product['name']}: ${product['price']}")


if __name__ == "__main__":
    main()
