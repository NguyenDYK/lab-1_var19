"""
Вариант 19.
Натуральные числа, расположенные в порядке не убывания.
Для каждого числа повторяющиеся цифры вывести прописью.
"""
numbers={0:"ноль" ,1:"один",2:"два", 3:"три", 4:"четыре", 5:"пять",
         6:"шесть", 7:"семь", 8:"восемь", 9:"девять" }
array=[]
work_buffer=""
buffer_len=1
k=0
flag=True
print("START")
try:
    with open ("text.txt", "r") as file: #откррывает файл
        buffer=file.read(buffer_len)  #читает првый блок
        if not buffer:
            print("Файл text.txt в директории проекта пустой. \nДобавьте не пустой файл в директорию или преобразуйте существующий *.txt файл")
        while buffer:
            while buffer!=" " and buffer!="\n" and buffer!="":
                if buffer>="0" and buffer<="9":
                    work_buffer+=buffer
                else: flag=False
                buffer=file.read(buffer_len)
                
            if len(work_buffer)>0 and flag==True:

    
                for i in range(len(work_buffer)):
                    array=[]
                    for a in range(10):
                        a=str(a)
                        if work_buffer.count(a)>=2:
                            a=int(a)                    
                            array.append(numbers[a])            
                if array==[] and int(work_buffer)>=k:
                    k=int(work_buffer)
                    print(work_buffer)
                elif int(work_buffer)>=k:
                    k=int(work_buffer)
                    print(work_buffer, "- повторяющиеся цифры:", ", ".join(array) + ".")

            work_buffer=""
            buffer=file.read(buffer_len)
            flag=True

except FileNotFoundError:
    print("\nФайл text.txt в директории проекта не обнаружен. \nДобавьте файл в директорию или переименуйте существующий файл *.txt файл.")
print("END")
