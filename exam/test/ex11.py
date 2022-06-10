word = input()
letter = input()
true = "Это слово оканчивается на эту букву"
false = "Увы!"

if word[-1]==letter:
    print(true)
else:
    print(false)