"""
#計算データの入力
amount=int(input('支払総額を入力してください:'))
people=int(input('参加人数を入力してください:'))

#割り勘の計算
dnum=amount/people#総額を人数で割る(端数保持)
pay=dnum//100*100#100￥未満を切り捨て
if dnum > pay:#元の値と比較して
    pay=int(pay+100)#小さければ100円未満があったので上乗せ

#幹事の支払額の計算
payorg=amount-pay*(people-1)

#結果表示
print('***支払額***')
print('1人あたり{}￥({}人)、幹事は{}￥です'
        .format(pay,people-1,payorg))
"""
def int_input(msg):
    return int(input('{}を入力してください:'.format(msg)))
def calc_payment(amount,people=2):
    dnum=amount/people
    pay=dnum//100*100
    if dnum > pay:
        pay=pay+100
    payorg=amount-pay*(people-1)
    return [int(pay),int(payorg)]
def show_payment(pay,payorg,people=2):
    print('***支払額***')
    print('1人あたり{}￥({}人)、幹事は{}￥です'
            .format(pay,people-1,payorg))
amount=int_input('支払総額');people=int_input('参加人数')
[pay,payorg]=calc_payment(amount,people)
show_payment(pay,payorg,people)
