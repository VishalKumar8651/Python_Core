import time 
#TIME MODULE USING
current_time = time.localtime().tm_hour
if current_time<12:
    print("Good Morning")
elif current_time>12 and current_time<16:
    print("Good Afternoon!!")
elif current_time>16 and current_time<20:
    print("Good Evening")
elif current_time>20 and current_time<24:
    print("Good Night")
