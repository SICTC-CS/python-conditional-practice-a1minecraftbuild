import random

cardType = random.randint(0,3)
cardNumber = random.randint(0,12)

cardList = ["Ace",2,3,4,5,6,7,8,9,10,"Jack","Queen","King"]
cardTypeList = ["Clubs","Diamonds","Hearts","Spades"]

print(f"You pulled out a {cardList[cardNumber]} of {cardTypeList[cardType]}!")
