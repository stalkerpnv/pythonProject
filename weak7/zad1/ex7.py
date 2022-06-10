n = int(input())
setA = set(range(1, n + 1))
posNumbers = setA
while True:
    guess = input()
    if (guess == 'HELP'):
        break
    else:
        answer = input()
        guess = set(map(int, guess.split()))
        if answer=='YES':
            posNumbers&=guess
        else:
            posNumbers-= setA-guess
print(' '.join([str(x) for x in sorted(posNumbers)]))
