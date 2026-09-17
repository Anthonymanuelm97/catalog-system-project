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
