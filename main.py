from pprint import pprint
def get_count_line_from_file (file_name):
    count = 0

    with open(file_name) as file:
        for _ in file:
            count += 1
        _file = [count, file_name]
        return _file


list_file = ['1.txt', '2.txt', '3.txt']
list_date = []
for name_file in range(len(list_file)):

    date = get_count_line_from_file(list_file[name_file])
    list_date.append(date)

list_date.sort()
print(list_date)

def get_date_from_file(file_name):
    count = 0
    list_q = " "
    with open(file_name) as file:
        for line in file:
            count += 1
            list_q += (line.strip() + " (строка № " + str(count) + f' файла {file_name})' "\n")

        return list_q


resultat = ' '
for file in range(len(list_date)):
        name = list_date[file][1]
        count_str = list_date[file][0]

        res = f'{name}\nКол-во строк {count_str}\n' + get_date_from_file(name)
        resultat += res
pprint(resultat)
def get_write_file(file_write,date_for_write):
    with open(file_write, 'w') as file:
        file.write(date_for_write)

get_write_file('answer_to_the_task.txt', resultat)



