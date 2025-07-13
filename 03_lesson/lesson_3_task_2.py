from smartphone import Smartphone

catalog = [
    Smartphone("Apple", "iPhone 13 PRO MAX", "+79123456789"),
    Smartphone("Apple", "iPhone 15 PRO MAX", "+79234567890"),
    Smartphone("Samsung", "Galaxy S24 Ultra", "+79345678901"),
    Smartphone("Google", "Pixel 7", "+79456789012"),
    Smartphone("Huawei", "P50 Pro", "+79567890123")
]

for phone in catalog:
    print(f"{phone.brand} - {phone.model}. {phone.phone_number}")