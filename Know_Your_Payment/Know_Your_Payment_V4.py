# %%
#If you work and receive your payment per hour, this can be useful, at least for me to train :)
#Edit: It is true that you received a raise?

def computepay(hour, rate) : 
    regular = hour * rate

    if hour > 40:
        extra = (hour - 40) * (rate * 0.5)
        total = extra + regular
        print('Seems that you are working a lot, consider a break ಠ⌣ಠ')
    else:
        total = regular
    
    return (round(100*total)/100)


try:
    hour = float(input('How mutch hours did you worked?\n'))
    per_h = float(input('How mutch do you receive per hour?\n'))
except:
    print("Hum, you do know it's tricky to predict what you will type, help me this time by using a number")
    quit()

payment = computepay(hour, per_h)

print('You shuld expect find $', payment,'in your bank (or maybe in you pocket [̲̅$̲̅(̲̅ ͡° ͜ʖ ͡°̲̅)̲̅$̲̅])')
