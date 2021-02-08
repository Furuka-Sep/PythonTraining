#点数の入力
def input_scores(name):
    print('{}さんの試験結果を入力してください'.format(name))
    network=int(input('ネットワークの得点…'))
    database=int(input('データベースの得点…'))
    security=int(input('セキュリティの得点…'))
    scores=[network,database,security]
    return scores#戻り値
#平均点を計算
def calc_average(scores):
    avg=sum(scores)/len(scores)
    return avg
#結果の出力
def output_result(name,avg):
    print('{}さんの平均点は{}です'.format(name,avg))
#実行
name=input('名前を入力…')
scores=input_scores(name)
avg=calc_average(scores)
output_result(name,avg)
