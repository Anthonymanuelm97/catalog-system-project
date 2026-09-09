business_catalog = [
    {"name": "massage", "price": 500.00, "available": True},
    {"name": "manicure", "price": 200.00, "available": True},
    {"name": "pedicure", "price": 300.00, "available": False},
]

def main():
    while True:
        print("Menu:")
        print("0. Salir")

        opcion = input("Elige una opción: ")

        if opcion == "0":
            print("Hasta luego!")
            break


if __name__ == "__main__":
    main()
