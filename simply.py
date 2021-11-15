#file này sẽ chạy toàn bộ chương trình

#import gói aiml để chạy
from os import truncate
import aiml

# vào cmd gõ lệnh pip install aiml để cài đặt aiml cho máy


kernel =  aiml.Kernel()

kernel.learn("std-startup.xml")



kernel.respond("LOAD AIML B")




while True:
    
     input_text = input(">Human: ")
     
     response = kernel.respond(input_text)
     
     print(">Bot: "+response)
