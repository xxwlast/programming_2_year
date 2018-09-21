import random

def opening(text):
    with open(text, encoding='UTF-8') as f:
        s = f.read()
        split = s.split('\n')
        #print(split)
    return split

def word(line):
    li = line.split(', ')
    #print(li)
    return random.choice(li)    
    
def retrieve_word(lines):
    iinput = ''
    while iinput not in ['1','2','3']:
        iinput = input('введите одну из трёх тем: виды напитков из кофе, районы Москвы, домашние растения: ')
        if iinput == '1':
            a = word(lines[0])
            #print(word(lines[0]))
        elif iinput == '2':
            a = word(lines[1])
            #print(word(lines[1]))
        elif iinput == '3':
            a = word(lines[2])
            #print(word(lines[2]))
        else:
            print("попробуйте ещё раз")
    return a

def hide(word):
    hidden = word.replace(word[1:], ' - '*(len(word)-1))
    q = print(hidden)
    return q

def answer(ask):
    input_letter = input('Введите букву: ')
    if input_letter == 

    

def main():
    print(answer(hide(retrieve_word(opening("C://Users//student//Desktop//program1.txt")))))
    
if __name__ == "__main__":
    main()
