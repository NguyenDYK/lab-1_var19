"""
Вариант 19.
Натуральные числа, расположенные в порядке не убывания.
Для каждого числа повторяющиеся цифры вывести прописью.
"""
import re
numbers={'0':"ноль" ,'1':"один",'2':"два", '3':"три", '4':"четыре", '5':"пять",
         '6':"шесть", '7':"семь", '8':"восемь", '9':"девять" }
array=[]
buffer_len=1
k=0
print("Начало")
try:
    file=open ("text.txt", "r") #откррывает файл
    while True:
        buffer=file.readline().split() #читает првый блок
        if not buffer:
            print("Конец.")
            break
        for j in buffer:
            r=re.findall(r'\d+',j)
            a=''.join(r)
            if len(r)==1:
                if len(j)==len(r[0]):
                    for i in range(len(r)):
                        array=[]
                        for a in range(10):
                            a=str(a)
                            if r[i].count(a)>=2:                    
                                array.append(numbers[a])
                        if array==[] and int(r[0])>=k:
                            k=int(r[0])
                            print(r[0])
                        elif int(r[0])>=k:
                            k=int(r[0])
                            print(r[0], "- повторяющиеся цифры:", ", ".join(array) + ".")
except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен. \nДобавьте файл в директорию или переименуйте существующий файл *.txt файл.")
