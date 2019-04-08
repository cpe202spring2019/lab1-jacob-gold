
def max_list_iter(int_list):  # must use iteration not recursion
   """finds the max of a list of numbers and returns the value (not the index)
   If int_list is empty, returns None. If list is None, raises ValueError"""
   
   max_val = 0
   if int_list == None: #checks for if int_list is None
      raise ValueError
   else:
      if len(int_list) == 0: #checks if int_list is empty
         return None
      else: 
         for i in int_list: #checks every value in int_list
            if i >= max_val: #checks if i is greater or equal to max_val in case of duplicates
               max_val = i #sets max_val equal to i
         return max_val

def reverse_rec(int_list):   # must use recursion
   """recursively reverses a list of numbers and returns the reversed list
   If list is None, raises ValueError"""
   
   if int_list == None:
      raise ValueError
   else:
      if len(int_list) != 0:
         appendValue = int_list.pop(0)
         reverse_rec(int_list)
         int_list.append(appendValue)
      else:
         return None
      return int_list
         

def bin_search(target, low, high, int_list):  # must use recursion
   """searches for target in int_list[low..high] and returns index if found
   If target is not found returns None. If list is None, raises ValueError """

   if int_list == None:
      raise ValueError
   if int_list == []:
      return None
   if low <= high:
      mid = (high+low)//2
      if target == int_list[mid]:
         return mid
      elif target < int_list[mid]:
         high = mid - 1
         return bin_search(target, low, high, int_list)
      else:
         low = mid + 1
         return bin_search(target, low, high, int_list)
      
   else:
      return None
