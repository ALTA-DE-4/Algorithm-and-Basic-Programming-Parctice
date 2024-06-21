def play_with_asterisk(n):
    for i in range(1, n + 1):
        print(' ' * (n - i), end='')
        print('* ' * i)

play_with_asterisk(5)
