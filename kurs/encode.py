import pickle
from generator import *

"""Генератор адресов несуществующих людей"""

name_dict = {}
for i in range(100):
    if name_dict.get(random_name()) is None:   
       name_dict[random_name()] = [random_address(),(random_phone(),random_phone()),(random_email(),),random_messanger()]

try:
    f = open('address_book', 'wb')
    f.write(pickle.dumps(name_dict))
    f.close()
except FileNotFoundError:
            print('No such file')
except IOError:
    print('Smth went wrong')
except OSError:
    print('OS goes mad, you see?')
except Exception as e:
    print('Unknown exception', e)

                 
    

