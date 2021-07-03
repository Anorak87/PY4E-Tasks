# %%

try:
    fhandle = open('mbox-short.txt')
except:
    print("Oh man, here are you blowing up my code again. This time you will fix (▀̿Ĺ̯▀̿ ̿)")
    print("\nIf you didn't changed anything check how you are runing the code, please run python3 in the same folder were is located de file. VS Code, for an example, runs python archieves from your top hierarchy level all the way down and this wasn't working here. I tryed Jupyter extension and it got the right path. Never forget the old and good terminal ┬┴┬┴┤ ͜ʖ ͡°) ├┬┴┬┴.")
    quit()

for line in fhandle:
    line = line.rstrip().upper()
    print(line) 
