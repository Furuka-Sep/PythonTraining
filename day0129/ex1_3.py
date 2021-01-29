"""
h=int(input('身長(cm):')) / 100
w=float(input('体重(kg):'))
bmi=w/h/h
print('BMI:{}'.format(bmi))
"""
h,w=int(input('身長(cm):'))/100,float(input('体重(kg):'))
print(f'BMI:{w/h**2 :.1f}')
