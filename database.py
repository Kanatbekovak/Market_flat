

raw_apartaments = [
    {
        "id": 1, 
        "district": "Issyk-Kul", 
        "price": 40000,   # Пишем просто число для расчетов
        "area": 65,        # м2
        "rooms": 4, 
        "floor": 1,       # Если дома частные, можно ставить 1
        "year": 2020
    },
    {
        "id": 2, 
        "district": "Bishkek", 
        "price": 55000, 
        "area": 42, 
        "rooms": 2, 
        "floor": 5, 
        "year": 2018
    },
    {
        "id": 3, 
        "district": "Bishkek", 
        "price": 10000, 
        "area": 42, 
        "rooms": 2, 
        "floor": 5, 
        "year": 2018
    },
    {
        "id": 4, 
        "district": "Bishkek", 
        "price": 100000, 
        "area": 42, 
        "rooms": 2, 
        "floor": 5, 
        "year": 2018
    },
    {
        "id": 5, 
        "district": "Bishkek", 
        "price": 75000, 
        "area": 42, 
        "rooms": 2, 
        "floor": 5, 
        "year": 2018
    },
    {
        "id": 6, 
        "district": "Issyk-Kul", 
        "price": 35000, 
        "area": 42, 
        "rooms": 2, 
        "floor": 5, 
        "year": 2018
    },
    {
        "id": 7, 
        "district": "Bishkek", 
        "price": 66000, 
        "area": 42, 
        "rooms": 2, 
        "floor": 5, 
        "year": 2018
    },
    {
        "id": 8, 
        "district": "Bishkek", 
        "price": 90000, 
        "area": 42, 
        "rooms": 2, 
        "floor": 5, 
        "year": 2018
    },
    {
        "id": 9, 
        "district": "Bishkek", 
        "price": 72000, 
        "area": 42, 
        "rooms": 2, 
        "floor": 5, 
        "year": 2018
    },
    {
        "id": 10, 
        "district": "Issyk-Kul", 
        "price": 58000, 
        "area": 42, 
        "rooms": 2, 
        "floor": 5, 
        "year": 2018
    }
]

for raw_apartament in raw_apartaments:
    if raw_apartament['id'] == 5:
        print(f"{raw_apartament["price"]}")

#////////////////////////////////////////////////////////////////////////////////

def calculate_average_price(list):
    average_price = []
    for item in list:
        if item["price"] > 0:
            average_price.append(item["price"])

    return sum(average_price) / len(average_price)

all_average = calculate_average_price(raw_apartaments)
print(f"Средняя цена на рынке: {all_average}")

#////////////////////////////////////////////////////////////////////////////////

def calculate_sq_meter_price(list, id):
    for item in list:
        if item["id"] == id:
            if item["area"] > 0:
                metr_price = item["price"] / item["area"]
                return round(metr_price, 2)
    return "Квартира с таким ID не найдена"

apartments_id = int(input("Enter your home: "))

metr_price = calculate_sq_meter_price(raw_apartaments, apartments_id)
print(f"Цена за 1м2 для {apartments_id} равна {metr_price}")

#/////////////////////////////////////////////////////////////////////////////////

def list_control(list,id):
    for item in list:
        if item["id"] == id:
            disti = item["district"]
            metr_price2 = round(item["price"] / item["area"], 2)
            return metr_price2, disti
    return None, None       

apartments_id = int(input("Enter your home: "))
metr_price2, disti = list_control(raw_apartaments,apartments_id)
if disti:
    print(f"Район {disti}, цена за метр {metr_price2}")
else:
    print("Квартира не найдена!")

#/////////////////////////////////////////////////////////////////////////////////

def evaluate_investment(list, id, average):
    for item in list:
        if item["id"] == id:
            price_home = item["price"]

            low_border = average * 0.85
            high_border= average * 1.15

            if price_home <= low_border:
                status = "Выгодно"
            elif price_home >= high_border:
                status = "Дорого"
            else:
                status = "Рыночная цена"
            
            return status, price_home
    
    return None, None

apartments_id = int(input("Enter your home: "))
status, price = evaluate_investment(raw_apartaments,apartments_id,all_average)

if status:
    print(f"Квартира №{apartments_id}")
    print(f"Цена:{price}$")
    print(f"Статус: {status}")
else:
    print("Неправильное введение")

for item in raw_apartaments:
    status_price, price_home = evaluate_investment(raw_apartaments,item["id"],all_average)
    item["status"] = status_price


for item in raw_apartaments:
    print(f"{item["id"]}, | {item["district"]}, | {item["status"]}")


# print(raw_apartaments[0])

#/////////////////////////////////////////////////////////////////////////////////

total_profit = 0 # копилка

for item in raw_apartaments:
    price_buy = int(item["price"] * 0.8)
    profit_price = int(item["price"] - price_buy)
    item["buyout_price"] = price_buy
    item["profit"] = profit_price
    total_profit += profit_price

for item in raw_apartaments:
    print(f"{item["id"]}, | Выкуп $ {item["buyout_price"]}, | прибыль $ {item["profit"]}")

print(f"Общая прибыль агенства: {total_profit}$")
# print(raw_apartaments[0])
