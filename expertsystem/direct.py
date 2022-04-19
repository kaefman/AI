from pyknow import *

class Anime(KnowledgeEngine):
    result = []

    @Rule(Fact('Нравятся сериалы'),
           OR(Fact('Хочется остановиться на одном произведении надолго'),Fact('Много свободного времени в день')))
    def long_series(self):
        self.declare(Fact('длительный сериал'))
        
    @Rule(OR(Fact('про дружбу'),Fact('про товарищество'),Fact('про командную работу')))
    def collective(self):
        self.declare(Fact('коллектив'))

    @Rule(OR(Fact('про драки'),Fact('про войну')))
    def battle(self):
        self.declare(Fact('сражение'))
    
    @Rule(OR(Fact('Предпочитаешь фильмы'),Fact('Много свободного времени в день')))
    def film(self):
        self.declare(Fact('фильм'))

    @Rule(Fact('спорт'),Fact('школа'),Fact('коллектив'),Fact('длительный сериал'))
    def voleyball(self):
        self.declare(Fact(anime='волейбол'))
        
    @Rule(Fact('экшен'),Fact('коллектив'),
          Fact('сражение'),
          Fact('длительный сериал'))
    def titans(self):
        self.declare(Fact(anime='атака титанов'))

    @Rule(Fact('длительный сериал'),
          Fact('психология'),
          Fact('детектив'))
    def deathnote(self):
        self.declare(Fact(anime='тетрадь смерти'))

    @Rule(Fact('психология'),
          Fact('сркажение'))
    def parasite(self):
        self.declare(Fact(anime='паразит: учение о жизни'))

    @Rule(Fact('коллектив'),
          Fact('школа'))
    def city(self):
        self.declare(Fact(anime='город в котором меня нет'))

    @Rule(Fact('нравится жанр романтика'))
    def god(self):
        self.declare(Fact(anime='очень приятно, бог'))

    @Rule(Fact('фильм'),
          Fact('нравится жанр романтика'),
          Fact('школа'))
    def yourname(self):
        self.declare(Fact(anime='твое имя'))

    @Rule(Fact('нравится жанр романтика'),
          Fact('фильм'),Fact('нужно детское аниме'))
    def castle(self):
        self.declare(Fact(anime='ходячий замок'))
        
    @Rule(Fact(anime=MATCH.a))
    def print_result(self,a):
        self.result.append(a)
        print('Аниме - {}'.format(a))
                    
    def factz(self,l):
        for x in l:
            self.declare(x)

user_ans=[]
my_questions={'Предпочитаешь фильмы?':['0.да','1.нет'],'Много свободного времени в день?':['0.да','1.нет'],'Нравятся сериалы?':['0.да','1.нет'],
'Хочется остановиться на одном произведении надолго?':['0.да','1.нет'],'нравится жанр романтика?':['0.да','1.нет'],
'школа?':['0.да','1.нет'],'спорт?':['0.да','1.нет'],'психология?':['0.да','1.нет'],'детектив?':['0.да','1.нет'],'экшен?':['0.да','1.нет'],'нравятся произведения про дружбу?':['0.да','1.нет'],
'про товарищество?':['0.да','1.нет'],'про командную работу?':['0.да','1.нет'],'про войну?':['0.да','1.нет'],'про драки?':['0.да','1.нет'],'нужно детское аниме?':['0.да','1.нет']}

def print_list(my_list):
    for el in my_list:
        print(el)

for key in my_questions.keys():
    print(key)
    print_list(my_questions[key])
    user_answer=input()
    user_answer_list=[]
    for l in my_questions[key]:
        if l.find(user_answer+'.')>-1:
            user_answer_list=l.split('.')
    if user_answer_list[1]=='да':
        user_ans.append(key[:-1])
    elif user_answer_list[1]!='нет' :
        user_ans.append(user_answer_list[1])

facts = []

for i in range(0,len(user_ans)):
    facts.append(Fact(user_ans[i]))

ex1 = Anime()
ex1.reset()
ex1.factz(facts)
ex1.run()
if len(ex1.result)==0:
    print('Мы не смогли подобрать для вас идеальное аниме :(')
print(ex1.facts)