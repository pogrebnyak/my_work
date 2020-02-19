from search import *

def print_table(data_dict,text):
    data_list = []
    s_list = []
    if data_dict == {}:
        print("СОВПАДЕНИЙ НЕ НАЙДЕНО")
    else:
        for i,j in data_dict.items():
            s_list = [i[0],i[1],i[2],j[0]]
            s_list.extend([x for x in j[1]])
            s_list.extend([x for x in j[2]])
            for a,b in j[3].items():
                s_list.extend([f'{a}: {b}'])
            data_list.append(s_list)
            
        sh = []        
        for i in data_list[0]:
            sh.append(0)
            
        for i in data_list:
            t = 0
            for j in i:
                if len(j) > sh[t]:
                    sh[t] = len(j)
                t += 1
           
        line_length = 0
        h = 0
        print (text)
        for i in data_list:
            line = ''
            t = 0
            line_length = 0
            for j in i:
                line_length += sh[t] + 2
                line += f'{j:{sh[t]}}  '
                t += 1
                if '@' in j:
                    break
            if h == 0:
                print(line_length * '-')
                h = 1
            print(line)
        print(line_length * '-')

        try:       
          f = open('address_result.txt', 'w')
          
          h = 0
          for i in data_list:
              line = ''
              t = 0
              line_length = 0
              for j in i:
                  line_length += sh[t] + 2
                  line += f'{j:{sh[t]}}  '
                  t += 1
              if h == 0:
                  f.write(text+'\n')
                  f.write(line_length * '-' + '\n')
                  h = 1
              f.write(line+'\n')
          f.write(line_length * '-' + '\n')
        
          f.close()
        except FileNotFoundError:
            print('No such file')
        except IOError:
            print('Smth went wrong')
        except OSError:
            print('OS goes mad, you see?')
        except Exception as e:
            print('Unknown exception', e)
   
while True:
  print('\n1. Поиск по Фамилии.')
  print('2. Поиск по Имени.')
  print('3. Поиск по ФИО.')
  print('4. Поиск по Реквизитам.')
  print('5. Сохранить список контактов.')
  print('6. Выход.')
  y = input(':')
  if y == '1': 
      print_table(*search_surname(input('Введите Фамилию: ')))
  if y == '2': 
      print_table(*search_name(input('Введите Имя: ')))
  if y == '3': 
      print_table(*search_3name(input('Введите ФИО: ')))
  if y == '4':
      print_table(*search_requisites(input('Введите реквизиты: ')))
  if y == '5':
      file_save()
  if y == '6':
      base_y = input('Хотите сохранить список перед выходом (y/n): ')
      if base_y == 'y':
          file_save()
      break
  

