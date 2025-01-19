from typing import Callable
import timeit
from pathlib import Path
from boyer_moore_search import boyer_moore_search
from kmp_search import kmp_search
from rabin_karp_search import rabin_karp_search

url1 = Path('./task_3/стаття_1.txt')
url2 = Path('./task_3/стаття_2.txt')



def read_file(filename: str) -> str:
    content = ''
    for encoding in ['utf-8', 'windows-1251']:
        try: 
            with open(filename, 'r', encoding=encoding) as fh:
                content = fh.read()
                print(f'Файл {filename}, відкрито за допомогою кодування {encoding}')
                print(50 * '-')
                break
        except Exception as e:
            pass
            # print(f'Помилка відкриття файла {filename} {e}') 
    
    return content

text_1 = read_file(url1)
text_2 = read_file(url2)



def measure_time(method, text, pattern):
    return timeit.timeit(lambda: method(text, pattern), number=10000)



patterns = {
    'existing': 'висновки',
    'non_existing': 'вигаданий підрядок'
}


results = []

for patterns_type, pattern in patterns.items():
    for i, text in enumerate([text_1, text_2],1):
        bm_time = measure_time(boyer_moore_search,text, pattern)
        kmp_time = measure_time(kmp_search,text, pattern)
        rk_time = measure_time(rabin_karp_search,text, pattern)


        results.append((f'Текст {i} - {patterns_type}', bm_time, kmp_time, rk_time))

for result in results:
    article, bm_time, kmp_time, rk_time, = result
    print(f"{article}: Boyer_Moore = {bm_time:.6f}s, KMP = {kmp_time:.6f}s, Rabin_Karp = {rk_time:.6f}s")







