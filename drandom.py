import threading
import time
import math
import signal
import sys

event = threading.Event()

with open('data.log', 'r') as file:
    content = file.read()
if content == "":
    t = time.time()
    # print(f"\033[1;34;40m DaYe: {int(round(t * 1000)) - int(t) * 1000} \033[0m")
    start_value = int(round(t * 1000)) - int(t) * 1000
    # print(f"\033[1;42m{start_value}\033[0m")
    with open('data.log', 'w') as file:
        file.write(str(start_value))
else:
    start_value = int(content)
    # print(f"\033[1;41m{start_value}\033[0m")

def main():
    global start_value
    while start_value <= 1000:
        start_value += 1
        if start_value > 1000:
            start_value = 2

def process(value):
    source = math.log(value)
    source = str(source).split('.')[1]
    t = time.time()
    begin = int(str(int(round(t * 1000000)) - int(round(t * 1000))*1000)[-2:])
    x_value = begin % len(source)
    if x_value + 8 > len(source):
        result = int(source[x_value:] + source[:8 - len(source[x_value:])])
    else:
        result = int(source[x_value:x_value+8])
    return result

def save_data(signum, frame):
    global start_value
    with open('data.log', 'w') as file:
        file.write(str(start_value))
    sys.exit(0)

def run():
    main_threading = threading.Thread(target=main, )
    main_threading.start()
    signal.signal(signal.SIGINT, save_data)
    signal.signal(signal.SIGTERM, save_data)

def get():
    global start_value
    return process(start_value)



'''
if __name__ == '__main__':
    main_threading = threading.Thread(target=main,)
    main_threading.start()
    
    while 1:
        x = input(">>>")
        if x == "get":
            print(f"\033[1;42m {get()} \033[0m")
'''