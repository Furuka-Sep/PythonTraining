def eat(**kwargs):
    for key in kwargs:
        print('{}に{}をたべた'
                .format(key,kwargs[key]))
eat(朝食='かに',遅めの昼食='にく',夕方のおやつ='くるみ')
