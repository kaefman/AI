class Ask():
    def __init__(self,choices=['Да','Нет']):
        self.choices = choices
    def ask(self):
        if max([len(x) for x in self.choices]) > 1:
            for i,x in enumerate(self.choices):
                print("{0}. {1}".format(i,x))
            x = int(input())
            return self.choices[x]
        else:
            print("/".join(self.choices))
            return input()

class Content():
    def __init__(self,x):
        self.x=x
        
class If(Content):
    pass

class AND(Content):
    pass

class OR(Content):
    pass

rules = {
    'default': Ask(['y','n']),
    'жанр' : Ask(['романтика','школа','спорт', 'психология', 'детектив', 'экшен']),
    'коллектив': If(OR(['дружба','товарищество', 'командная работа'])),
    'сражение': If(OR(['война','драка'])),
    'длительный сериал': If(['нравятся сериалы',OR(['хочется остановиться на одном произведении надолго \
            ','много свободного времени в день'])]),
    'фильм': If(OR(['предпочитаешь фильмы','много свободного времени в день'])),
    'аниме:волейбол' : If(['коллектив','длительный сериал','жанр:школа', 'жанр:спорт']),
    'аниме:атака титанов' : If(['жанр:экшен','коллектив','сражение','длительный сериал']),
    'аниме:тетрадь смерти' : If(['жанр:психология','жанр:детектив','длительный сериал']),
    'аниме:паразит: учение о жизни' : If(['жанр:психология','сражение']),
    'аниме:город в котором меня нет' : If(['жанр:школа','коллектив']),
    'аниме:очень приятно, бог' : If(['жанр:романтика']),
    'аниме:твоё имя' : If(['жанр:романтика','жанр:школа','фильм']),
    'аниме:ходячий замок' : If(['жанр:романтика','фильм','для детей'])
}


class KnowledgeBase():
    def __init__(self,rules):
        self.rules = rules
        self.memory = {}

    def get(self,name):
        if name in self.memory.keys():
            return self.memory[name]
        for fld in self.rules.keys():
            if fld==name or fld.startswith(name+":"):
                # print(" + proving {}".format(fld))
                value = 'y' if fld==name else fld.split(':')[1]
                res = self.eval(self.rules[fld],field=name)
                if res=='y':
                    self.memory[name] = value
                    return value
        # field is not found, using default
        res = self.eval(self.rules['default'],field=name)
        self.memory[name]=res
        return res

    def eval(self,expr,field=None):
        if isinstance(expr,Ask):
            print(field)
            return expr.ask()
        elif isinstance(expr,If):
            return self.eval(expr.x)
        elif isinstance(expr,AND) or isinstance(expr,list):
            expr = expr.x if isinstance(expr,AND) else expr
            for x in expr:
                if self.eval(x)=='n':
                    return 'n'
            return 'y'
        elif isinstance(expr,OR):
            for x in expr.x:
                if self.eval(x)=='y':
                    return 'y'
            return 'n'
        elif isinstance(expr,str):
            return self.get(expr)
        else:
            print("Unknown expr: {}".format(expr))


kb = KnowledgeBase(rules)
print(kb.get('аниме'))
