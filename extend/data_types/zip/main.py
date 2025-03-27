fruits = ['apple', 'banana', 'orange']
prices = {100, 200, 300}
quantity = '12312'
availability = (True, False, True)

for fruit, price in zip(fruits, prices):
    print(f"{fruit}: {price}")

print('========================================')
fruits_prices = zip(fruits, prices)
print(fruits_prices)
fruits_prices = dict(fruits_prices)
# print(list(fruits_prices))
print(fruits_prices)
print('========================================')


print(list(fruits_prices))
fruits_prices = zip(fruits, prices, availability, quantity)

print(fruits_prices)
print(id(fruits_prices))
print(type(fruits_prices))
print(list(fruits_prices))


