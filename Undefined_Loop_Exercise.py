count = 0
total = 0
error = True

number = input("Type a Number: ")

while number != "done" :
    try :
        number = int(number)
    except:
        print("Not a Number: ")
        error = False

    if error :
        count += 1
        total += number

    error = True
    number = input("Type a Number: ")

print(total, count, total/count)
