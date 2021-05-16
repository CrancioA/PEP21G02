def conversation():
    name = None
    name1 = 'John'
    def hello():
        print('Hello,', name1, '!')
    def response_hello():
        nonlocal name
        name = input('My name is ')
    def question():
        print(name ,', how is the weather?', sep='')
    def question2():
        print('The weather is sunny! How old are you,', name1, '?' )
    def answer():
        print("I'm 15 years old." )
    return hello, response_hello, question, question2, answer

c = conversation()
c[0]()
c[1]()
c[2]()
c[3]()
c[4]()
