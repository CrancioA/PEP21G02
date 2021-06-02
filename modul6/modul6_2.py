# open

# file = open('my_file.txt', 'w')
# file.write('My new text\n')
# file.close()
#
# with open('my_file.txt', 'a') as file:
#     file.write('Random text')
#
# print(type(file))

# class MyError(Exception):
#     pass
# try:
#     1/0
# except MyError:
#     print('expert')
# finally:
#     print("we have an error")

# class A():
#     _test = 'protected'
#     __test = 'private' # variabila privata
#
#     def __init__(self):
#         self.__ts()
#
#     def _ts(self):
#         print('_')
#
#     def __ts(self):
#         self.__test += '__'
#
# a = A()
# print(a._test)
# # asa se acceseaza variabila privata
# print(a._A__test)
# print(a._ts())
# print(a._A__ts())

#lambda
my_functions = []
for i in range(10, 100):
    def check(a):
        if a < i:
            return True
        else:
            return False
    my_functions.append(check)

my_functions = []
for i in range(10, 100):
    my_functions.append(lambda a: True if a < i else False)
    print(my_functions)