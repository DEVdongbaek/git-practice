def do_fizzbuzz(num:int):
    for i in range(1, num+1):
        if i%3 == 0:
            print('hello')
        
        elif i%5 ==0:
            print('buzz')
        
        elif i%15==0:
            print('pizzbuzz')

        else:
            print(f'{i}')


if __name__ == '__main__':
    do_fizzbuzz(16)
