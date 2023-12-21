#Написать программу, которая из имеющегося массива строк формирует новый массив из строк, длина которых меньше, либо равна 3 символам. 
#Первоначальный массив можно ввести с клавиатуры, либо задать на старте выполнения алгоритма. 
#При решении не рекомендуется пользоваться коллекциями, лучше обойтись исключительно массивами.

def fltr (animals, lenght= 3):
    result = []

    for animal in animals:
        if len(animal) <= lenght:
            result.append(animal)

    return result


animals = ['Cat', 'Wolf', 'Elephant', 'Lion', 'Dog', 'Rabbit', 'Lizard', 'Bear']
result = fltr(animals)

print(f'Original list:\n'
      f'{animals}.\n\n'
      f'Filtered list:\n'
      f'{result}.')