# Схожие слова
# Напишите программу, которая находит все схожие слова для заданного слова. Слова называются схожими,
# если имеют одинаковое количество и расположение гласных букв. При этом сами гласные могут различаться.
#
# Формат входных данных
# На вход программе подается одно слово, записанное в первой строке, затем натуральное число
# n — количество слов для сравнения и n строк со словами.
#
# Формат выходных данных
# Программа должна вывести все схожие слова для заданного слова, сохранив их исходный порядок следования.
#
# Примечание 1. После последней гласной в начальном и проверяемом слове может быть любое количество согласных.
#
# Примечание 2. В русском языке
# 10 гласных букв (а, у, о, ы, и, э, я, ю, ё, е) и
# 21 согласная буква (б, в, г, д, ж, з, й, к, л, м, н, п, р, с, т, ф, х, ц, ч, ш, щ).

gl = ('а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е')

main_word = input()
main_word_gl = tuple(i for i in range(len(main_word)) if main_word[i] in gl)

n = int(input())
result = []

for _ in range(n):
    word = input()
    if main_word_gl == tuple(i for i in range(len(word)) if word[i] in gl):
        result.append(word)

for i in result:
    print(i)
