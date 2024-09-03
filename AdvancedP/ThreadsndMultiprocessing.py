#Threads vs Multiprocessing

#Process-The program in execution
#Thread- lightweight process running faster than process also occypy separate memory

#Lock -allows to run only one thread at a time becoz memory management is not thread safe in  python also it avoid multiprocessing

from threading import Thread
from multiprocessing import Process
import os
import time

# def square_number():
#   for i in range(100):
#     i=1
#     time.sleep(0.1)

# processes=[]
# num_processes=os.cpu_count()

# #create process
# for i in range(num_processes):
#     p=Process(target=square_number)
#     processes.append(p)

# #start
# for p in processes:
#   p.start()

# #join
# for p in processes:
#   p.join()

# print('end main')


def square_number():
  for i in range(100):
    i=1
    time.sleep(0.1)

threads=[]
num_threads=os.cpu_count()

#create process
for i in range(num_threads):
    t=Thread(target=square_number)
    threads.append(t)

#start
for t in threads:
  t.start()

#join
for t in threads:
  t.join()

print('end main')


