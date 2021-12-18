def max_heapify(arr, length, i):

    largest = i
    l = 2 * i + 1 # lchild of i-th node @ 2i + 1
    r = 2 * i + 2 # rchild of i-th node @ 2i + 2
  
    # Find largest between left and right child
    
    if l < length: # Bounds checking
      if arr[largest] < arr[l]:
        largest = l

    if r < length: # Bounds checking
      if arr[largest] < arr[r]:
        largest = r

    # Swap root with largest if different
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]

        # Recursive max heapification of roots
        max_heapify(arr, length, largest)

    # When the code reaches this line, the array is heapified
