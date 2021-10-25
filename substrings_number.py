string = "avava avavava" #"01000100101010 0101 0101010001"
substring = "vav" #"01"

#вычисляем длину подстроки для извлечения срезов, ищем совпадение подстроки со срезои строки,
# если совпадает, увеличиваем счетчик и продолжаем итерацию по следующим элементам
counter = 0

for i in range(len(string) - len(substring) + 1):
    if string[i:i + len(substring)] == substring:
        counter +=1

print(counter, len(string) - len(substring) + 1, len(string))
