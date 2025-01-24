import random


print("Я загадал число (от 1 до 9).Сможете угадать?")
comp_number=random.randint(1,10)

user_number=int(input(" "))
cnt_user=0
ishora=True
while ishora:
    
    if comp_number==user_number:
        print(f"Бингоо!  Я думал о числе {comp_number}, Вы нашли его с {cnt_user} попыток.Поздравляю!!")
        ishora=False
        
    if user_number>comp_number:
        print("Ошибка, мое загадданое число меньше этого. Попробуйте еще раз:")
        cnt_user+=1
        user_number=int(input(" "))

    if user_number<comp_number:
        print("Ошибка, мое загадданое число больше этого. Попробуйте еще раз:")
        cnt_user+=1
        user_number=int(input(" "))


print("")
print("")
print("")


print("Задумайте число от 1 до 10. Я попробую его найти.")
print("Если вы задумали , нажмите любую кнопку...")
print("")

low=1
high=10
cnt_computer=0

while True:
    comp_number = random.randint(low, high)
    cnt_computer += 1
    print(f"Число, которое я задумал: {comp_number}.")
    user_input = input("Правильно (T), задуманное  число больше (+) или меньше (-), чем это: ").lower()

    if user_input == 't':
        print(f"Я угадал  {cnt_computer}-(й,ой) попытки!")
        break

    elif user_input == '+':
        low = comp_number + 1

    elif user_input == '-':
        high = comp_number - 1

    else:
        print("Пожалуйста введите '+' или '-' или 'T'")


print("")
print("")

#Yakun
if cnt_user<cnt_computer:
    print(f"Вы нашли мое число с {cnt_user} попыткой и выиграли!")
elif cnt_user>cnt_computer:
    print(f"Йесс,Я победил с {cnt_computer} попыткой ")
else:
    print("Ничья. Победила дружба.!!!")

print("")
print("")