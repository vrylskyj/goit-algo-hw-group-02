from collections import deque

def is_palindrome(s):
    # Видаляємо пробіли та перетворюємо рядок у нижній регістр
    s = s.replace(" ", "").lower()
    
    # Створюємо двосторонню чергу та додаємо до неї символи рядка
    char_queue = deque(s)
    
    # Порівнюємо символи з обох кінців черги
    while len(char_queue) > 1:
        if char_queue.popleft() != char_queue.pop():
            return False
    
    # Якщо всі символи були однаковими, то рядок - паліндром
    return True

# Приклад використання
input_string = "A man a plan a canal Panama"
print(is_palindrome(input_string))  # Виведе True