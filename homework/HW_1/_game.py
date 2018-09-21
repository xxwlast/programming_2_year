def game(word, hidden_word):
    letters = 'йцукенгшщзхъфывапролджэячсмитьбюё'
    a = ''
    tries = 5
    result = ''
    with open ('viselitsa.txt', encoding = 'utf-8') as f:
        pics = f.read()
        picss = pics.split('\n\n')
        
    while result == '':
        a = input("Введите букву: ").lower()
        if a in letters:
            if len(a) == 1:
                #print(a)
                if a in word:
                    print('Поздравляем, вы отгадали!')
                    #написать замену: регулярками (заёбно), или можно тупо как у меня замена побуквенно
            
                    
                else:
                    print('Сорян')
                    tries -= 1
                    #колво попыток
                    
                    
            else:
                print('Это не буква, попробуйте снова')
        else:
            print('Это не буква, попробуйте снова')
    if tries == 0:
        result = 'К сожалению, Вы проиграли.'
    if '-' not in hidden_word:
        result = 'Ура, Вы победили!'
        
    return result    

    
def main():
    print(game('Ховрино','Х -  -  -  -  -  - '))
if __name__ == "__main__":
    main()
    
