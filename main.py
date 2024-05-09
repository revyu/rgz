import os 
import subprocess


name=input("Введите имя файла ")


# Выполнение команды "dir /r" с помощью subprocess
streams = subprocess.run(["cmd", "/c", "dir", "/r"], capture_output=True, text=True)

# Получение вывода команды
output = streams.stdout


output=output.split("\n")

streams=[]
s=0
for i in output:
    if name in i:
        _=i.split()# имя файла потока всегда идет последним перед ним его размер в байтах
        streams.append(_[-1])
        s+=int(_[-2])
          



for i in streams:
   print(i)
   os.system(f"more< {i}") 
print(f"суммарный размер файла:{s}")



