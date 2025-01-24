import random


print("1 dan 10 gacha son o'yladim.Topa olasizmi?")
comp_number=random.randint(1,10)

user_number=int(input(" "))
cnt_user=0
ishora=True
while ishora:
    # print("1 dan 10 gacha son o'yladim.Topa olasizmi?")
    if comp_number==user_number:
        print(f"TOPDINGIZ! {comp_number} sonini o'ylagan edim,{cnt_user} ta taxmin bilan topdingiz.Tabriklayman!!")
        ishora=False
        
    if user_number>comp_number:
        print("Xato,men o'ylagan son bundan kichikroq.Yana harakat qiling:")
        cnt_user+=1
        user_number=int(input(" "))

    if user_number<comp_number:
        print("Xato,men o'ylagan son bundan kattaroq.Yana harakat qiling:")
        cnt_user+=1
        user_number=int(input(" "))


print("")
print("")
print("")


print("1 dan 10 gacha son o'ylang.Men topishga harakat qilaman")
print("Son o'ylagan bo'lsangiz istalgan tugmani bosing. ")
print("")

low=1
high=10
cnt_computer=0

while True:
    comp_number = random.randint(low, high)
    cnt_computer += 1
    print(f"Men o'ylagan son: {comp_number}.")
    user_input = input("To'g'ri (T), men o'ylagan son bundan kattaroq (+), yoki kichikroq (-): ").lower()

    if user_input == 't':
        print(f"Siz soningizni {cnt_computer}-chi urinishda topdim!")
        break

    elif user_input == '+':
        low = comp_number + 1

    elif user_input == '-':
        high = comp_number - 1

    else:
        print("Iltimos, faqat '+' yoki '-' yoki 'T' ni kiriting.")


print("")
print("")

#Yakun
if cnt_user<cnt_computer:
    print(f"Siz {cnt_user} ta taxmin bilan topdingiz va  yutdingiz")
elif cnt_user>cnt_computer:
    print(f"Men {cnt_computer} ta taxmin bilan yutdim")
else:
    print("Durrang.Do'stlik g'alaba qozondi!!!")

print("")
print("")