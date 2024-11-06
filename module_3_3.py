#задача 1 Функция с параметрами по умолчанию
# def print_params(a = 1, b = 'строка', c = True):
#     print(a, b, c)
# print_params (b=25, c = [1, 2, 3])


# # 2.Распаковка параметров:
# values_list = ['строка', 34, False]
# values_dict = {'a':1, 'b':'строка', 'c' : True}
# def print_params (a, b, c):
#     print(a, b, c)
# print_params (*values_list)
# print_params (**values_dict)

# 3.Распаковка + отдельные параметры:

values_list_2 = [67, 'klop']
def print_params (a, b, c):
    print(a, b, c)
print_params (*values_list_2, 544 ) # консоль: 67 klop 544



