# %%
#If you work and receive your payment per hour, this can be useful, at least for me to train :)
#Edit: It is true that you received a raise?
try:
    hour = float(input('How mutch hours did you worked? '))
    per_h = float(input('How mutch do you receive per hour? '))
except:
    print("Hum, you do know it's tricky to predict what you will type, help me this time by using a number")
    quit()
#Could be done diferent but I think it's easier to think like that
regular = hour * per_h
if hour > 40 : 
    extra = (hour - 40) * (per_h * 0.5)
    total = extra + regular
    print('Seems that you are working a lot, consider a break ಠ⌣ಠ')
else :
    total = regular

total = (round(100*total)/100)
print('You shuld expect find $', total,' in your bank (or maybe in you pocket [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅])')

#I know that is prety simple to add verifications for what the user typed but this time I was trying the "Try/Except"
