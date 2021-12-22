##Digite este exemplo em um script e teste-o
def do_twice(function):
    function()
    function()

def print_spam():
    print('spam')

do_twice(print_spam)

#altere do_twice para receber dois argumentos: um objeto de função e um valor e chame a função duas vezes, passando o vallor como um argumentos

def do_twiceUpdated(function, arg):
    function(arg)
    function(arg)



do_twice(print,"whatsapp")