# 키보드에서 정수로 된 돈의 액수를 입력 받아 오만 원권, 만원 권, 오천 원권, 천원 권,
# 500원짜리 동전, 100원짜리 동전, 50원짜리 동전, 10원짜리 동전, 1원짜리 동전 각 몇 개로 변환
# 되는지 작성하시오.

money = int(input('금액 : '))

print(f'50000원 : {money//50000}개')
money %= 50000
print(f'10000원 : {money//10000}개')
money %= 10000
print(f'5000원 : {money//5000}개')
money %= 5000
print(f'1000원 : {money//1000}개')
money %= 1000
print(f'500원 : {money//500}개')
money %= 500
print(f'100원 : {money//100}개')
money %= 100
print(f'50원 : {money//50}개')
money %= 50
print(f'10원 : {money//10}개')
money %= 10
print(f'1원 : {money}개')