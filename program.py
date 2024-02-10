import random, time
random.seed(time.time())
count = 0
while True:
    try:
        print('--------------------------------------')
        num = random.randrange(0, 4294967295)
        print('The current integer:', num)
        guess = int(input('Guess the next integer: '))
        next_int = random.randrange(0, 4294967295)
        if guess == next_int:
            print('Correct')
            count += 1
        else:
            print('Incorrect')
        print('The next integer:', next_int)
        if count == 10:
            print('RPCA-UNICEF{md5}')
            break
    except:
        break
        