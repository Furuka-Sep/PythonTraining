class Hero:
    name='浅木'
    hp=100
    def sleep(self,hours):
        print('{}は{}時間寝た！'.format(self.name,hours))
        self.hp+=hours

#gamestart
print('スッキリファンタジーXVI ～金色のおふとぅん～')
h = Hero()
h.sleep(2)
print('{}のHPは現在{}です'.format(h.name,h.hp))
