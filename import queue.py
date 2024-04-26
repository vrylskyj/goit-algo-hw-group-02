import queue
import time
import threading

# Створення черги заявок
request_queue = queue.Queue()

# Функція для генерації заявок
def generate_request():
    while True:
        # Генерація нової заявки (уявимо, що це якась інформація про замовлення)
        new_request = "New request"
        
        # Додавання заявки до черги
        request_queue.put(new_request)
        print("Generated new request:", new_request)
        
        # Затримка для імітації випадкового часу між заявками
        time.sleep(2)

# Функція для обробки заявок
def process_request():
    while True:
        if not request_queue.empty():
            # Видалення заявки з черги
            request = request_queue.get()
            print("Processing request:", request)
            # Імітація обробки заявки
            time.sleep(1)
        else:
            print("No requests to process")
            # Затримка, щоб не перевантажувати процесор
            time.sleep(1)

# Створення та запуск потоків для генерації та обробки заявок
generate_thread = threading.Thread(target=generate_request)
process_thread = threading.Thread(target=process_request)

generate_thread.start()
process_thread.start()

# Очікуємо завершення потоків (це необхідно лише для демонстрації, на практиці можливі інші способи завершення програми)
generate_thread.join()
process_thread.join()