import multiprocessing
import time
def read_info(name):
    #создаем список
    all_data = []
    #открываем файл для чтения
    with open(name, 'r') as file:
        line = file.readline()
        #нам нужен это цикл пока строка не пустая
        while line:
            all_data.append(line.strip()) #здесь добавляем строку в список
            line = file.readline()

if __name__ == '__main__':
  filenames = [f'./file {number}.txt' for number in range(1, 5)]

  #Линейный вызов
  #start_time = time.time()
  #for filename in filenames:
    #read_info(filename)
  #end_time = time.time()
  #print(f"{time.strftime('%H:%M:%S', time.gmtime(end_time - start_time))}")

  # Многопроцессный
  start_time = time.time()
  with multiprocessing.Pool(processes=4) as pool:
      pool.map(read_info, filenames)
  end_time = time.time()
  print(f"{time.strftime('%H:%M:%S', time.gmtime(end_time - start_time))}")