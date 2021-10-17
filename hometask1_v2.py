users_list = [
    ['George', 'Hart', 22],
    ['Edward', 'Jackson', 19],
    ['Jessica', 'James', 21],
    ['Joseph', 'Ellis', 19],
    ['Christopher', ' Olson', 22],
    ['Lynn', 'Anderson', 19],
    ['William', 'Noble', 18],
    ['Ashley', 'Griffin', 21],
    ['Michael', 'Sawyer', 22],
    ['Amanda', 'Rodriguez', 19],
    ['Brandi', 'Armstrong', 22],
    ['Christopher', 'Vazquez', 18],
    ['Joseph', 'Christopher', 21],
    ['David', 'Porter', 19],
    ['Angelica', 'Bell', 23],
    ['Rebecca', 'Hudson', 18],
    ['Nicole', 'Weaver', 19],
    ['Cindy', 'White', 22],
    ['David', 'Compton', 20],
    ['Rodney', 'Lara', 24]
]
#quest1
# print('Покупатели старше 21 года:')
# for a, b, c in users_list:
#     if c >= 21:
#         print(a, b, c)

#quets2
# a = float(input())
# b = a
# a = a ** 3 - a / 2
# a = round(a, 2)
# print(f'Для Х = {b} значение функции = {a}')

#quest3
for a, b, c in users_list:
    if a.startswith('A'):
        print(a, b, c)
