import time

class masterClass:
  
  @classmethod 
  def quickSort(cls, LIST): 
    '''learned and understood Quick Sorting algorithm logic from Youtube Video: 
      https://www.youtube.com/watch?v=kFeXwkgnQ9U&t=1s'''
    if len(LIST) <= 1:
      return LIST
    
    Lesser, Greater, Equal = [],[],[] 

    #Selecting the middle of the list as a Pivot Point
    middle = int((len(LIST)-1)/2)
    Pivot = LIST[middle]

    #QuickSorting Process
    for element in LIST:
      if element < Pivot: #elements less than pivot appended into Lesser
        Lesser.append(element)
      elif element == Pivot: #elements equal to pivot appended into Equal
        Equal.append(element)
      else:  #elements greater than pivot appended into Greater
        Greater.append(element)
    
    LIST = cls.quickSort(Lesser) + Equal + cls.quickSort(Greater) #Sorting the list
    return LIST
    
  @classmethod
  def selectionSort(cls, LIST):
    '''learned and understood Selection Sorting algorithm logic from article below: 
       https://www.geeksforgeeks.org/python-program-for-selection-sort/'''
    for i in range(len(LIST)-1):
      Minimum = i #Assigning the first index as Minimum 

      for element in range(i+1, len(LIST)): #Starts from the next value of the index assigned
        if LIST[Minimum] > LIST[element]: #Constantly changing the value of Minimum to arrange the list
          Minimum = element 

      (LIST[i], LIST[Minimum]) = (LIST[Minimum], LIST[i]) #Swapping the element to sort the list
    return LIST
  
  @classmethod
  def mergeSort(cls, LIST):
    '''learned and understood Merge Sorting algorithm logic from article below: 
       https://www.programiz.com/dsa/merge-sort'''
    if len(LIST) > 1:
      middle = int(len(LIST) / 2) #Finding the Middle Point
      Left = LIST[:middle] #Assigning the left of Middle point to the variable "Left"
      Right = LIST[middle:] #Assigning the right of Middle point to the variable "Right"

      #Recursion to break down left and right lists
      cls.mergeSort(Left)
      cls.mergeSort(Right)

      l, r, i = 0, 0, 0

      #Sorting Process-------
      #While we have arguments in the both right and left list
      while l < len(Left) and r < len(Right): 
        if Left[l] <= Right[r]: 
          LIST[i] = Left[l] #Adds the left elements to the 'LIST' 
          l += 1
        else: 
          LIST[i] = Right[r] #Adds the right elements to the 'LIST'
          r += 1
        i += 1 #index goes to the next value

      #Checks for other values that have been left out
      while l < len(Left):
        LIST[i] = Left[l] #Adds the left elements to the 'LIST' 
        l += 1
        i += 1
    
      while r < len(Right):
        LIST[i] = Right[r] #Adds the right elements to the 'LIST' 
        r += 1
        i += 1

    return LIST