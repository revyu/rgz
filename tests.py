import os

with open("file.txt", "w") as file:
    
    file.write("this is main stream\n")
   
    os.system("echo this is extended stream > file.txt:stream_name")
    os.system("echo 1 >file.txt:stream_name2")

    
with open("file_no_ext_streams.txt", "w") as file:
    
    file.write("this is main stream\n")

with open("file_no_main_stream.txt", "w") as file:
    
    os.system("echo this is extended stream > file_no_main_stream.txt:stream_name")
    
