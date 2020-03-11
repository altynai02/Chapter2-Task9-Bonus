# BONUS
# 3.Напишите программу (используя функции!), Которая запрашивает у пользователя
# длинную строку, содержащую несколько слов. Выведите обратно пользователю ту же
# строку, Но уже в обратном порядке. Например, скажем, я набрал строку:
# My name is Emir
# Output:
# Emir is name My

def reverse():
    text = " " # обратно в строку с пробелом
    your_text = input("Enter your text: ").split()
    your_text = list(your_text)
    your_text.reverse()
    print(text.join(your_text))

reverse()