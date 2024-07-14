import time
import drandom

drandom.run()       # launch drandom
delay = 0.1

if __name__ == '__main__':
    for i in range(1000):
        time.sleep(delay)
        value = drandom.get()
        print(f"\033[1;42m {value} \033[0m")

