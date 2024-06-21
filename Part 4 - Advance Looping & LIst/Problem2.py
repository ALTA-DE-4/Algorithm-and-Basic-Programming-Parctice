def draw_xyz(N):
    for i in range(1, N * N + 1):
        if i % 3 == 0:
            print("X", end=" ")
        elif i % 2 == 0:
            print("Z", end=" ")
        else:
            print("Y", end=" ")
        
        if i % N == 0:
            print()  


draw_xyz(3)
print('---------------------------')
draw_xyz(5)
