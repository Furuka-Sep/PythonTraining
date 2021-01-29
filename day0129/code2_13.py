scores={'network':60,'database':80,'security':50}
print(scores)
print(scores['database'])
scores['programming']=65#要素追加
scores['security']=55#要素の変更
scores['ああああ']='いいいい'
print(scores)
del scores['ああああ']#要素の削除
print(scores)
print(sum(scores.values()))#キー無しで値のみ表示
