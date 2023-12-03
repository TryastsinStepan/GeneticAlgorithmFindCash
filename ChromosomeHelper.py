from Individual import  *
#Файл, содержащий вспомогательные методы для кодирования и декодирования хромосом
#Метод для кодирования объекта Individual в строку хромосомы
def encode_individual_to_chromosome(invividual:Individual) -> str:
    #Преобразование весов объекта Individual в двоичный формат их представления
    weight_1_binary = bin(invividual.get_weight1())[2:]
    weight_2_binary = bin(invividual.get_weight2())[2:]
    weight_3_binary = bin(invividual.get_weight3())[2:]

    #Объединение двоичных представлений весов в одну строку хромосомы
    chromosome = weight_1_binary+weight_2_binary+weight_3_binary
    return chromosome #Возвращает строку хромосомы

#Метод для декодирования строки хромосомы в объект Individual
def decode_chromosome_to_individual(chromosome:str) -> Individual:
    #Разделение строки хромосомы на три части, соответствующие весам Individual
    weight_1_binary = chromosome[:8]
    weight_2_binary = chromosome[8:16]
    weight_3_binary = chromosome[16:]

    #Преобразование двоичных представлений весов в числа
    weight1 = int(weight_1_binary,2)
    weight2 = int(weight_2_binary,2)
    weight3 = int(weight_3_binary,2)
    return Individual(weight1,weight2,weight3) #Возвращает новый объект Individual

#Метод для преобразования десятичного числа в его двоичное представление в виде строки
def decimal_to_binary(decimal_number:int) ->str:
    #Преобразование десятичного числа в его двоичное представление, дополняя нулями слева до 8 символов
    return '0'*(8-len(str(decimal_number))) + str(decimal_number)

#Метод для преобразования двоичной строки в десятичное число
def binary_to_decimal(binary_number: str) -> int:
    #Преобразование двоичной строки в десятичное число
    decimal_number = int(binary_number,2)
    return decimal_number #Возвращает десятичное число