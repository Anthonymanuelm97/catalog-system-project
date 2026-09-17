def menu(business):
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
            business.view_catalog()

        if option == "2":
            name_searched = input("Enter the product name: ")
            product = business.search_product(name_searched)

            if product is not None:
                print(product)
            else:
                print("product not found")

        if option == "3":
            name = input("Enter the product name: ")
            price = input("Enter the product price: ")
            available = input("Is it available? (True/False): ") == "True"

            new_product = business.add_product(name, price, available)
            print(f"Product added: {new_product}")

        if option == "4":
            available_catalog = business.available_product()
            for product in available_catalog:
                print(f"{product['name']}: ${product['price']}")
