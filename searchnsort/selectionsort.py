def selection_sort(arr):

    n = len(arr)

    for i in range(n-1):
        min_idx = i

        for j in range(i+1,n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        
        arr[i],arr[min_idx] = arr[min_idx],arr[i]
    
    print(arr)

selection_sort([1,9,7,3,4])