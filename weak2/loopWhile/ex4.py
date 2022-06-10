# Дано натуральное число N. Выведите слово YES, если число N является точной степенью двойки,
# или слово NO в противном случае. Операцией возведения в степень пользоваться нельзя!
#
N = int(input())
print("YES" if (N & (N - 1)) == 0 else "NO")