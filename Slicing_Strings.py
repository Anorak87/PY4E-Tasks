string = "X-DSPAM-Confidence: 0.8475 "

print("Today I will be safe from your bad inputs __.\n\nI'm trying some slicing strings.\nbetter try and fail now so in the future I will fail better\n\nAnyway, heres the string (I will take the final part and convert to float):", string, "\n")
start_position = string.find(":")
sliced_string = string[start_position+2:] # ignores de digit and the blank space
fl_from_str = float(sliced_string)
print("Result:", sliced_string)
print("Just to be sure that is a float (I will not die because I'm sure, right?)\nfl_from_str + 1 =", fl_from_str+1)

print("(I know this isn't the best way to confirm types)\n", type(fl_from_str))
#I will commit but will come back, I had some good ideas for cometaries today 