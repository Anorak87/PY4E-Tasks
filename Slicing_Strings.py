string = "X-DSPAM-Confidence: 0.8475 "

start_position = string.find(":")
sliced_string = string[start_position+2:]
fl_from_str = float(sliced_string)
print(sliced_string)

#I will commit but will come back, I had some good ideas for cometaries today