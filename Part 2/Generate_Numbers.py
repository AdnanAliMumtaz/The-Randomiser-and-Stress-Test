import random
import time
from MasterClass import masterClass

#Generating the randomised 7-digit numbers
def Generate_numbers(Range):
    return random.sample(range(1000000,9999999), Range)

#Writing to the Files
def Writing(FileName, List):
  Elements = []
  for i in List: #Storing the ints into string list
    Elements.append(str(i))
  
  with open(FileName, "w") as wfile:
    wfile.write(str("\n".join(Elements)))

#Calculating Runtime, Calling the sorting algorithm methods, Writing to a file
def Calling(list, sorting, Filename):
  starttime = time.time() #Records the initial time.
  
  #Calling the algorithm class method.
  sorted_list = sorting(list) 
  
  elapsedtime = time.time() - starttime #Calculating the elapsed time.

  #Writing the sorted list to file.
  Writing(Filename, sorted_list)

  random.shuffle(list) #Randomising the list after being sorted for next algorithm.

  #Printing the runtime for each algorithm
  print(str(elapsedtime) +  " (secs) for " + Filename.strip('.txt'))



#Calling Functions---------------
#Generating numbers and assigning to the variables.
First_list = Generate_numbers(10000)
Second_list = Generate_numbers(100000) 
Third_list = Generate_numbers(1000000) 

#QuickSorting Process
print("Quicksort Timings")
Calling(First_list, masterClass.quickSort, "Quicksort_small.txt")
Calling(Second_list, masterClass.quickSort, "Quicksort_mid.txt")
Calling(Third_list, masterClass.quickSort, "Quicksort_large.txt")
print('\n')

#SelectionSorting Process
print("Selectionsort Timings")
Calling(First_list, masterClass.selectionSort, "Selectionsort_small.txt")
Calling(Second_list, masterClass.selectionSort, "Selectionsort_mid.txt")
Calling(Third_list, masterClass.selectionSort, "Selectionsort_large.txt")
print('\n')

#MergeSorting Process
print("Mergesort Timing")
Calling(First_list, masterClass.mergeSort, "Mergesort_small.txt")
Calling(Second_list, masterClass.mergeSort, "Mergesort_mid.txt")
Calling(Third_list, masterClass.mergeSort, "Mergesort_large.txt")
print('\n')
