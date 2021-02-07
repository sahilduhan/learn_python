import random
import time

time_list = []
my_data = []

def save_time(exec_time):
    time_list.append(exec_time)

for i in range(int(1e4)):
    my_data.append(random.randint(0,9e4))

start_time = time.time()
my_data.sort(reverse = True) 
save_time((time.time() - start_time))

# start_time = time.time()
# my_data.sort()
# save_time((time.time() - start_time))

for time in time_list:
    print("--- %s seconds ---" % time)