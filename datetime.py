import random
from datetime import datetime

now = datetime.now()
if now.hour < 12:
    print("Good Morning!")
elif now.hour < 18:
    print("Good Afternoon!")
else:
    print("Good Evening!")
print(f"Today's date : {now.day}/{now.month}/{now.year}")
print(f"Today's time : {now.hour}:{now.minute}:{now.second}s")