text = input('何を記録しますか>>')
file = open('dialy.txt','a')
file.write(text + '\n')
file.close()
