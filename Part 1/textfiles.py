import random

#Handling & Processing the Files----------------
def Files(Filename):
    #Reading, Shuffling and Triming
    with open(Filename, "r") as R_file:
        Names = R_file.readlines()
    random.shuffle(Names)
    del Names[4000:]

    #Stripping the '\n' from each element in list
    for i in range(4000): 
        Names[i] = Names[i].strip()
    
    #Writing to the File after Triming
    WritingFile(Filename, Names)

    print("Lenght of " + Filename + " : " + str(len(Names)))
    return Names

#Writing to the Files----------------
def WritingFile(Filename, list): 
    with open(Filename, "w") as W_file:
        W_file.write("\n".join(list)) #'\n'.join to arrange names in 4000 lines

#Generating a List of FullNames----------------
def Generate_fullname(Firstnames, Lastnames):
    Fullnames = []
    for i in range(4000):
        Fullnames.append(Firstnames[i] + " " + Lastnames[i])
    random.shuffle(Fullnames) #Randomising the Fullnames

    WritingFile("fullNames.txt", Fullnames) #Writing the Fullnames file
    return Fullnames

#Recursion to Count the Frequency of each element----------------
def Counting(Name):
    if Name: 
        return 1 + Counting(Name[1:]) #Returns 1, goes over the rest of the name 
    return 0 

#Calculating the Longest Name----------------
def Largest_name(Fullnames):
    Counter = []
    #Iteration to go through the fullnames list 
    for name in Fullnames:
        Counter.append(Counting(name)) #Calling the recursive function
    
    #Figures out the index of the largest value in the list 
    Index = Counter.index(max(Counter))
    print("Largest Name: '" + Fullnames[Index] + "' with " + str(max(Counter)) + " characters.")


#Calling Functions///////////////////////
FirstNames = Files("fileName.txt") #Returns the 4000 names from first file.
LastNames = Files("lastName.txt") #Returns the 4000 names from second file.
Fullnames = Generate_fullname(FirstNames, LastNames) #Returns the 4000 fullnames.
Largest_name(Fullnames) #Prints the largest name with characters. 