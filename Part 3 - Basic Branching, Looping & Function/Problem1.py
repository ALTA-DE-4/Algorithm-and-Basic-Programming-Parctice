student_score = 0.25

if 80 <= student_score <= 100:
    grade ='A'
elif 65 <= student_score <= 79:
    grade ='B+'
elif 50 <= student_score <= 64:
    grade ='B'
elif 35 <= student_score <= 49:
    grade ='C'
elif 0 == student_score <= 34:
    grade ='D'
else:
    grade = "-"

print(f'Nilai {grade}')
