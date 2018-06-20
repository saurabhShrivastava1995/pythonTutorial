print("Questions will apear on your screen see if you can anser those.")

file_des = open('questions.txt', 'r')
questions = [line.strip() for line in file_des.readlines()]
file_des.close()
count = 0
total = 0
for question in questions:
    (ques,ans) = question.split('=')
    user_ans = input(ques + " = ")
    if user_ans == ans:
        count += 1
    total += 1
file_des = open('result.txt', 'w')
file_des.write(f'Your final score is {count}/{total}')
file_des.close()