#Алгоритм работы кода:

# Импорты необходимых модулей и функций
# Объявление функции write_words
# Взятие текущего времени
# Запуск функций с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы функций
# Взятие текущего времени
# Создание и запуск потоков с аргументами из задачи
# Взятие текущего времени
# Вывод разницы начала и конца работы потоков

from time import sleep, time
import threading

def write_words(word_count, file_name):
    with open(file_name, 'w') as file:
        for i in range(1, word_count+1):
            file.write(f'Какое-то слово № {i}\n')
            sleep(0.1)
    print(f'Завершилась запись в файл {file_name}')

#записали текущее время в переменную
start_time = time()
write_words(10, 'example1.txt')
write_words(30, 'example2.txt')
write_words(200, 'example3.txt')
write_words(100, 'example4.txt')
end_time = time()

#выводим время потраченное на работу функций
print(f'Работа функций {end_time - start_time}')

def thread_write_words(word_count, file_name):
    write_words(word_count, file_name)

threads = []
start_time_threads = time()
for word_count, file_name in [(10, 'example5.txt'), (30, 'example6.txt'), (200, 'example7.txt'), (100, 'example8.txt')]:
    thread = threading.Thread(target=thread_write_words, args=(word_count, file_name))
    threads.append(thread)
    thread.start()

for thread in threads:
    thread.join()

end_time_threads = time()
print(f'Работа потоков {end_time_threads - start_time_threads}')


