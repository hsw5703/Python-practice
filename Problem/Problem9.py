# 주어진 if 문을 dict를 사용해서 수정하세요.

dict_menu = {'오뎅' : 300, '순대' : 400, '만두' : 500}
input_menu = input('어떤 메뉴 : ')
if input_menu in dict_menu :
    print(f'가격 : {dict_menu[input_menu]}')
else :
    print('없는 메뉴')