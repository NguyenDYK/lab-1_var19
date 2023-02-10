numbers={0:"ноль" ,1:"один",2:"два", 3:"три", 4:"четыре", 5:"пять", 6:"шесть", 7:"семь", 8:"восемь", 9:"девять" }
array=[]
try:
    with open ("text.txt", "r") as file:
        buffer=file.read().split()
##        print(buffer)
        if not buffer:
            print("Файл text.txt в директории проекта пустой. \nДобавьте не пустой файл в директорию или преобразуйте существующий *.txt файл")
        else:
            for i in range(0, len(buffer)):
                array=[]
##                print(buffer[i])
                for a in range(0, 10):
                    a=str(a)
                    if buffer[i].count(a)>=2:
                        a=int(a)
##                        print(a)                    
                        array.append(numbers[a])
                if array==[]:
                    print(buffer[i])
                else:
                    print(buffer[i], "- повторяющиеся цифры:", ", ".join(array) + ".")
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен. \nДобавьте файл в директорию или переименуйте существующий файл *.txt файл.")
