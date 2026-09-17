from business import Business
from interface import menu


def main():
    business_catalog = [
        {"name": "massage", "price": 500.00, "available": True},
        {"name": "manicure", "price": 200.00, "available": True},
        {"name": "pedicure", "price": 300.00, "available": False},
    ]

    business = Business(business_catalog)
    menu(business)


if __name__ == "__main__":
    main()
