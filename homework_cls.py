''' Product - класс, представляющий товар, с атрибутами name (название товара) и price (цена товара).
	Customer - класс, представляющий клиента, с атрибутами name (имя клиента) и orders (список заказов клиента).
	Order - класс, представляющий заказ, с атрибутом products (список товаров в заказе).
	Discount - класс для применения скидок, с атрибутами description (описание скидки) и discount_percent (процент скидки).
'''
class Product():
    def __init__(self, name:str, price:int) -> None:
        self.name = name
        self.price = price
        
    def __str__(self) -> str:
        return f"Товар {self.name} стоимостью {self.price}"
    
    def __eq__(self, value: object) -> bool:
        return self.price == value.price
  
    def __lt__(self, value):
        return self.price > value.price
  
    
class Discount():
    def __init__(self, description:str, discount_percent:int) -> None:
       self.description = description
       self.discount_percent = discount_percent
       
    # Используйте статические методы в классе Discount для расчета цены со скидкой 
    # и применения различных видов скидок (например, сезонная скидка, скидка по промокоду и т.д.).
    @staticmethod
    def get_new_price(price:int, ds:int):
        return price * (1-ds/100)
    
    def __str__(self) -> str:
        return f"{self.description} скидка"


class Order():
            
    def __init__(self, products:list=[], ds = Discount("Без скидок", 0)) -> None:
        self.products = products
        self.discount = ds
    
    def add_product(self, product:Product=[]):
        self.products.append(product)  
        
    @staticmethod
    def final_price_product(price:int, discont:int) -> float:
        return price * (1-discont/100)
    
    def total_sum(self):
        return sum([Discount.get_new_price(elem.price, self.discount.discount_percent) for elem in self.products])
    
    def __str__(self) -> str:
        return f"Товары: {[elem.name for elem in self.products]} на сумму: {self.total_sum()}. Применена скидка {self.discount.description}"

    def __len__(self):
        return len(self.products)
    
class Customer():
    def __init__(self, name:str, orders:list) -> None:
        self.name = name
        self.orders = orders
        self.total_orders = len(orders)
        self.total_sum = sum([order_cust.total_sum() for order_cust in self.orders])
    
    def add_orders(self, order:Order):
        self.orders.append(order)   
        self.total_orders += 1 
        self.total_sum += order.total_sum()
        
    def __str__(self) -> str:
        return f"Клиент {self.name}: {self.total_orders} заказов на сумму {self.total_sum}"
    
               
# Создайте несколько продуктов и клиентов    
d_summer = Discount("SUMMER", 10)
d_new_year = Discount("2025", 15)
tv1,tv2,nb = Product("TV", 5000), Product("TV", 6000), Product("Notebook", 15000)
or1, or2, or3 = Order([tv1, nb]), Order([tv1, tv2, nb]), Order([])
cl1,cl2,cl3 = Customer("Eldorado", [or1]), Customer("MVideo", [or2]), Customer("Ozon", [or3])

# Реализуйте функциональность для добавления заказов к клиентам
cl3.add_orders(or1)
cl3.add_orders(or2)

print("Проверка стоиомости двух товаров:")
if tv1 == tv2:
    print("Телевизоры одинаковые")
else:
    print("Телевизоры разные")
print()

# Примените различные виды скидок к заказам.
or1.discount = d_summer
print(f"Сумма заказа с учетом {or1.discount.description} скидки:  {or1.total_sum()}")
print()

# Подсчитайте общее количество заказов и общую сумму всех заказов для всех клиентов.
print(f"Всего заказов сделано: {cl1.total_orders + cl2.total_orders + cl3.total_orders} на общую сумму: {cl1.total_sum + cl2.total_sum + cl3.total_sum}")
print()

# Выведите информацию о клиентах, заказах и продуктах с использованием дандер методов
print("Общая информация")
print("1. Клиенты")
print(cl1, cl2, cl2, sep="\n")
print("2. Заказы")
print(or1, or2, or3, sep="\n")
print("3. Товары")
print(tv1,tv2,nb, sep="\n")


    
       