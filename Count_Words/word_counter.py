#recieve the file name
file_name = input("Type the file name: ")

#prepare for a bad input
try:

    file_handle = open(file_name)

except:
    file_name = 'clown.txt'
    file_handle = open(file_name)

#create a dictionary for the words
word_dict = dict()

#loop through every line
for line in file_handle : 
    #clean the line
    line = line.rstrip()
    #split the line
    word_list = line.split()

    #count words and put in a dictionary
    for word in word_list :
        word_dict[word] = word_dict.get(word, 0) + 1

#find the most common word

for k,v in word_dict.items() :
    if v is max(word_dict.values()) :
        mc_key = k
        mc_value = v

#user feedback

print("\nThe word '" + mc_key + "' appear", mc_value, "times in the", file_name)
print("Obs: This is the most common word in the file")
