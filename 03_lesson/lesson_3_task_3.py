from address import Address
from mailing import Mailing

to_addr = Address("123456", "Москва", "Ленина", "10", "15")
from_addr = Address("654321", "Санкт-Петербург", "Невский", "25", "8")
mailing = Mailing(to_addr, from_addr, 1500, "TR123456789RU")

print(f"Отправление {mailing.track} из {mailing.from_address.postal_code}, {mailing.from_address.city}, {mailing.from_address.street}, {mailing.from_address.house} - {mailing.from_address.apartment} в {mailing.to_address.postal_code}, {mailing.to_address.city}, {mailing.to_address.street}, {mailing.to_address.house} - {mailing.to_address.apartment}. Стоимость {mailing.cost} рублей.")