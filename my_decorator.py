# def obertka():
#     def hello_world():
#         print("Hello World!")
#     def good_bye():
#         print("Good Bye!")
#
#     hello_world()
#     good_bye()
# obertka()

def decorator_func(func):
    def obertka():
        print("обёртка")
        a=87
        print("оборачевамая функция: {}".format(func))
        print("выполняем обёрнутую функцию")
        for i in range(10):
            func(a)
        print("выходим из обёртки")
    return obertka

@decorator_func
def hello_world(a):
    b=6
    c=a+b
    print("Hello World!",c)
hello_world()


@decorator_func
def summa(a):
    b=50
    c=a+b
    print("сумма",c)
summa()


@decorator_func
def mult(a):
    b=30
    c=a*b
    print("произведение",c)
mult()