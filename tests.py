import os

name="file.txt"
with open("file.txt", "w") as file:
    
    file.write("eto osnovnoi potok\n")
   
    os.system("echo eto dopolnitelnii potok > file.txt:stream_name")
    os.system("echo 1 >file.txt:stream_name2")

    
with open("file_no_ext_streams.txt", "w") as file:
    
    file.write("eto osnovnoi potok\n")