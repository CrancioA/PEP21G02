# my_list = [1, 2, 3]
#
# for i in my_list:
#     print(i)
#
# iterator = my_list.__iter__()
# print(type(iterator))
# print(iterator.__next__())
# print(iterator.__next__())
# print(iterator.__next__())


class Shop:
    def __init__(self, products: list):
        self.products = products

    def __iter__(self):
        return ShopIterator(self.products.copy())


class ShopIterator:

    def __init__(self, products: list):
        self.products = products

    def __iter__(self):
        return self

    def __next__(self):
        if not self.products:
            raise StopIteration
        return self.products.pop()


shop = Shop(['books', 'bananas', 'water'])

for items in shop:
    print(items)

print('From constructor:', shop.products)
shop_iter = shop.__iter__()
print('First element:', shop_iter.__next__())
print('Second element:', shop_iter.__next__())
print('Third element:', shop_iter.__next__())


