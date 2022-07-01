import time
import random
start = time.time ()
time_out = False
wishes = []
print ("You have provide your answers in 10 seconds from now")
while not time_out:
    end = time.time ()
    if end - start < 10:
        t = int (10- (end-start))
        print ("You still have", t, "seconds")
        wish = input ("Tell me your wish?: ")
        wishes.append (wish)
    else:
        time_out = True
print("Your wishes are:", wishes)
randomwish = random.randint(0, len(wishes))
print("I grant you the wish:", wishes[randomwish])