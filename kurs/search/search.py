import pickle

def file_save():
    try:       
      f = open('./address_book', 'wb')
      f.write(pickle.dumps(obj))
      f.close()
      print('База успешно сохранена')
    except FileNotFoundError:
        print('No such file')
    except IOError:
        print('Smth went wrong')
    except OSError:
        print('OS goes mad, you see?')
    except Exception as e:
        print('Unknown exception', e)

def search_surname(surname):
    text = f'\nПоиск по фамилии: {surname}'
    surname_dict = {}
    for i,j in obj.items():
        if surname in i[0]:
            surname_dict[i] = j
    return surname_dict,text

def search_name(name):
    text = f'\nПоиск по имени: {name}'
    name_dict = {}
    for i,j in obj.items():
        if name in i[1]:
           name_dict[i] = j
    return name_dict,text
            
def search_3name(pib):
    text = f'\nПоиск по Фамилии Имени Отчеству: {pib}'
    pib_dict = {}
    for i,j in obj.items():
        if pib in f'{i[0]} {i[1]} {i[2]}':
           pib_dict[i] = j
    return pib_dict,text

def search_requisites(string):
    text = f'\nПоиск по реквизитам: {string}'
    requisites_dict = {}
    for i,j in obj.items():
        if string in str(j):
            requisites_dict[i] = j
    return requisites_dict,text

obj = {}
try:       
  f = open('./address_book', 'rb')
  obj = f.read()
  f.close()
  obj = pickle.loads(obj)
except FileNotFoundError:
    print('No such file')
except IOError:
    print('Smth went wrong')
except OSError:
    print('OS goes mad, you see?')
except Exception as e:
    print('Unknown exception', e)
