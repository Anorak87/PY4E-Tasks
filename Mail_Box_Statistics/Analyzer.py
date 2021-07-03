print("This time I will be counting the quantity of e-mails you get daily based on the archive mail-box_short.txt in this same folder:\n")


try:
    fhandle = open('mail-box_short.txt')
except:
    print("Oh man, here are you blowing up my code again. This time you will fix (▀̿Ĺ̯▀̿ ̿)")
    print("\nIf you didn't changed anything check how you are runing the code, please run python3 in the same folder were is located de file. VS Code, for an example, runs python archieves from your top hierarchy level all the way down and this wasn't working here. I tryed Jupyter extension and it got the right path. Never forget the old and good terminal ┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴")
    quit()

week_data = dict()

for line in fhandle:
    line = line.rstrip().upper() 
    # I'm keping .upper() because you may try to change the mail-box_short. I will get better on avoid you every day (ง'̀-'́)ง.
    line = line.split()

    if len(line) < 3 or line[0] != 'FROM':
        continue

    day = line[2]

    if day in week_data:
        week_data[day] = week_data[day] + 1
    else:
        week_data[day] = 1


frequency = 10000
free_day = None

for day,times in week_data.items():
    print(day,":",times)

    if frequency > times:
        free_day = day
        frequency = times

print("\nSeems that you can relax on", free_day + ".", "\nUnfortunately I can't, do you know why?")
print("Because I am tryng to get some money, but everything is ok, God is helping me ♥‿♥ and maybe one day I will relax like you on", free_day + ".")

    
