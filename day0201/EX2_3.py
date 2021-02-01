setA={'カラオケ','ゲーム','読書','料理','映画'}
setB={'カラオケ','ゲーム','バスケ','ショッピング','映画'}
input('心の準備ができたらEnterキーを押して下さい')
result=(len(setA & setB) / len(setA | setB))*100
print('2人の相性は',result,'%です')
