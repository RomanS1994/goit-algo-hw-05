import random
def created_arr(count):
    array = [round(random.uniform(1.5, 5.5), 1) for el in range(count)]
    return array


def binary_search(arr: list, x: float):
    low = 0
    high = len(arr) - 1
    mid = 0
    count = 0
 
    while low <= high:
        count += 1
        mid = (high + low) // 2 # індекс середини
 
        # якщо x більше за значення посередині списку, ігноруємо ліву половину
        if arr[mid] < x:
            low = mid + 1
 
        # якщо x менше за значення посередині списку, ігноруємо праву половину
        elif arr[mid] > x:
            upper_bound = arr[mid]
            high = mid - 1
        # інакше x присутній на позиції і повертаємо його
        else:
            return count, arr[mid]

    # Якщо елемент не знайдено, повертаємо верхню межу
    if upper_bound is None and low < len(arr):
        upper_bound = arr[low]  # Наступний більший елемент
    
    return count, upper_bound

def main():
    count = input('Введіть довжину масиву >>> ')
    array = created_arr(int(count))
    
    array.sort()
    print(f'Масив {array}')

    el = input('Введіть елемент для пошуку >>> ')
    iterations, upper_bound = binary_search(array, float(el))
    
    if upper_bound is not None:
        print(f'Кількість ітерацій: {iterations}, Верхня межа: {upper_bound}')
    else:
        print(f'Кількість ітерацій: {iterations}, Верхня межа не знайдена')



if __name__ == '__main__':
    main()

