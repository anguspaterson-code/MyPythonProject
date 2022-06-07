import random

YourTicket = random.sample(range(1,30), 7)
LotteryNum = random.sample(range(1,30), 7)


print("Your ticket numbers: ")
print(YourTicket)

print("The lottery numbers are: ")
print(LotteryNum)

check = any(item in YourTicket for item in LotteryNum)
print("Do you have winning numbers? : " + str(bool(check)))
