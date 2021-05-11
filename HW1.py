a = open('greetings.txt', 'w')

name = input('Введите имя пользователя:')

for i in range(10):
    a.write('Greeting'+ name + '\n')

def func():
    a.write('Ramazan')

func()

a.close()