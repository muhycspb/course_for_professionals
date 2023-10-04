# Файлы в файле
# Вам доступен текстовый файл files.txt, содержащий информацию о файлах.
# Каждая строка файла содержит три значения, разделенные символом пробела — имя файла,
# его размер (целое число) и единицы измерения:
#
# cant-help-myself.mp3 7 MB
# keep-yourself-alive.mp3 6 MB
# bones.mp3 5 MB
# ...
# Напишите программу, которая группирует данные файлы по расширению, определяя общий объем
# файлов каждой группы, и выводит полученные группы файлов, указывая для каждой ее общий объем.
# Группы должны быть расположены в лексикографическом порядке названий расширений, файлы в
# группах — в лексикографическом порядке их имен.
#
# Примечание 1. Например, если бы файл files.txt имел вид:
#
# input.txt 3000 B
# scratch.zip 300 MB
# output.txt 1 KB
# temp.txt 4 KB
# boy.bmp 2000 KB
# mario.bmp 1 MB
# data.zip 900 MB
# то программа должна была бы вывести:
#
# boy.bmp
# mario.bmp
# ----------
# Summary: 3 MB
#
# input.txt
# output.txt
# temp.txt
# ----------
# Summary: 8 KB
#
# data.zip
# scratch.zip
# ----------
# Summary: 1 GB
# где Summary — общий объем файлов группы.
#
# Примечание 2. Гарантируется, что все имена файлов содержат расширение.
#
# Примечание 3. Общий объем файлов группы записывается в самых крупных (максимально возможных)
# единицах измерения с округлением до целых. Другими словами, сначала следует определить суммарный объем
# всех файлов группы, скажем, в байтах, а затем перевести полученное значение в самые
# крупные (максимально возможные) единицы измерения. Примеры перевода:
#
# 1023 B -> 1023 B
# 1300 B -> 1 KB
# 1900 B -> 2 KB
# Примечание 4. Значения единиц измерения такие же, какие приняты в информатике:
#
# 1 KB = 1024 B
# 1 MB = 1024 KB
# 1 GB = 1024 MB

d = {}
f = open('files.txt', encoding='utf8')
f_sorted = [i.strip() for i in sorted(f.readlines(), key=lambda x: x.split()[0].split('.')[-1])]
f.close()
while f_sorted:
    file_name, file_size = f_sorted[0].split(' ', 1)
    file_extension = file_name.split('.')[-1]
    match file_size.split()[-1]:
        case 'B':
            file_size = int(file_size.split()[0])
        case 'KB':
            file_size = int(file_size.split()[0]) * 1024
        case 'MB':
            file_size = int(file_size.split()[0]) * 1024**2
        case 'GB':
            file_size = int(file_size.split()[0]) * 1024**3
        case 'TB':
            file_size = int(file_size.split()[0]) * 1024 ** 4
    if file_extension not in d:
        d[file_extension] = [[file_name], [file_size]]
    else:
        d[file_extension][0].append(file_name)
        d[file_extension][1] = [d[file_extension][1][0] + file_size]
    f_sorted.pop(0)
for key, values in d.items():
    for value in sorted(values[0]):
        print(value)
    print('----------')
    rounded = values[1][0]
    if rounded // 1024 < 1:
        rounded = str(rounded) + ' B'
    elif rounded // 1024 // 1024 < 1:
        rounded = str(round(rounded // 1024)) + ' KB'
    elif rounded / 1024 / 1024 / 1024 < 1:
        rounded = str(round(rounded / 1024 / 1024)) + ' MB'
    elif rounded // 1024 // 1024 // 1024 // 1024 < 1:
        rounded = str(round(rounded  // 1024 // 1024 // 1024)) + ' GB'
    elif rounded // 1024 // 1024 // 1024 // 1024 // 1024 < 1:
        rounded = str(round(rounded // 1024 // 1024 // 1024 // 1024)) + ' TB'
    print('Summary:', rounded)
    print()
