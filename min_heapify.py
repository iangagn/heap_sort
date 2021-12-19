def min_heapify(arr, length, i):
    '''
    Performs recursive min heapification.
    
    Parameters
    ----------
    arr : list, tuple or set
        An array.
        
    length : int
        Length of array.
        
    i : int
        Index of current (sub)tree root.
      
    Returns nothing.
    '''

    smallest = i
    l = 2 * i + 1 # lchild of i-th node @ 2i + 1
    r = 2 * i + 2 # rchild of i-th node @ 2i + 2
  
    # Find smallest between left and right child
    
    if l < length: # Bounds checking
      if arr[smallest] > arr[l]:
        smallest = l

    if r < length: # Bounds checking
      if arr[smallest] > arr[r]:
        smallest = r

    # Swap root with smallest if different
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]

        # Recursive min heapification of roots
        max_heapify(arr, length, largest)

    # When the code reaches this line, the array is heapified
