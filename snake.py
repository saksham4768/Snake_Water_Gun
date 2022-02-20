def for_result (re):

    if(user_choice==re):
        return "! DRAW !,Try again"
    elif(user_choice == "snake" and re == "water"):
        return "you won"
        
    elif(user_choice == "snake" and re == "gun"):
        return "you losse"
        
    elif(user_choice == "water" and re == "snake"):
        return "you loose"
        
    elif(user_choice == "water" and re == "gun"):
        return "you win"
        
    elif(user_choice == "gun" and re == "snake"):
        return "you win"
        
    elif(user_choice == "gun" and re == "water"):
        return "you loose"
        
    else:
        print("good luck")






import random
lst = ["snake","water","gun"]
won=0
losse=0
drawn=0
for i in range(10):
    user_choice = input(" 'snake - water - gun' ?:-\n")
    if user_choice=="snake" or user_choice=="water" or  user_choice=="gun":
        re = random.choice(lst)
        print("computer's choise....." +re)
        result = for_result(re)
        if result=="you win":
            won = won+1
        elif result == "! DRAW !,Try again":
            drawn=drawn+1
        else:
            losse = losse+1
        print(result)
    else:
        print("invalid key")
    
print("Number of times you won= "+ str(won))
print('\n')
print("Number of times you losse= "+ str(losse))
print('\n')
print("Number of times you drawn= "+ str(drawn))
if won>losse:
    print("Congratulations !! YOU WIN")
elif won== losse:
    print("Ohhhhh!! MATCH DRAWN")
else:
    print("! YOU LOSSE !,Better luck next time")





            