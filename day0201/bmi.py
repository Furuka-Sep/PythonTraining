height=input('身長(cm)を入力してください>')
weight=input('体重(kg)を入力してください>')
height=float(height)/100
weight=float(weight)
bmi=weight/(height*height)
print('BMI:',bmi)

#if文

if bmi>=25:
    result='肥満'
elif bmi>=18.5:
    result='標準体重'
else:
    result='痩せ型'
print(result,'x')
