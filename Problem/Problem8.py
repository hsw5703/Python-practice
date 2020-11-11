# 문자열을 입력 받아, 해당 문자열을 문자 순서를 뒤집어서 반환하는 함수 reverse(s)을
# 작성하세요.

str_input = input('입력> ')
list_input = list(str_input)
print(list_input)
list_input = [i for i in str_input]
print(list_input)

list_input.reverse()
str_input = ''.join(list_input)
print(f'출력> {str_input}')