import random
import string

def random_email():
    f = ('@gmail.com','@i.ua','@ukr.net','@mail.ru','@yahoo.com','@yandex.ua','@meta.ua')
    return random.choice(line) + random.choice(f)

def random_messanger():
    s = random.choice(line)
    f = dict(Skype=s,Telegram='@'+s)
    return f

def random_phone():
    f = ('050','066','067','068','097','098')
    return random.choice(f) + ''.join([random.choice(string.digits) for x in range(7)])

try: 
    f = open('generator/dictionary.txt','r')
    line = f.read().splitlines()
    f.close
except FileNotFoundError:
            print('No such file')
except IOError:
    print('Smth went wrong')
except OSError:
    print('OS goes mad, you see?')
except Exception as e:
    print('Unknown exception', e)


