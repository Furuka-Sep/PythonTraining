scores=[88,90,95]#List
scores.append(34)#要素の追加
scores.append(72)
scores.remove(72)#要素の削除
scores[0]=82#要素の変更
total=sum(scores)#要素の合計
avg=total/len(scores)#len=要素数
print(f'合計{total}点\n平均{avg:.1f}点')
