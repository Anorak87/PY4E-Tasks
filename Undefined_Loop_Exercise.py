count = 0
total = 0

while True :
    number = input("Type a Number: ")

    if number == "done" :
        break

    try :
        number = float(number)
    except:
        print("Not a Number: ")
        continue

    count += 1
    total += number

print("Total:", total, "\nSum:", count, "\nAvg:", total/count)

#Today I do not had any good ideas for great commentaries ¯\_(ツ)_/¯ 
