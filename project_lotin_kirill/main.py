from translatirate import to_cyrillic,to_latin

matn=input("Введите текст: ")

if matn.isascii():
    print(to_cyrillic(matn))
else:
    print(to_latin(matn))