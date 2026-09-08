
def quick_sort(arr,left,right):

    if left < right:
        p = partition(arr,low,high)

        quick_sort(arr,left,p-1)
        quick_sort(arr,p+1,right)
    

def partition(arr,low,high):


    pivot = arr[high]

    i = low - 1

    for j in range(low,high):
        if arr[j] < pivot:
            i+=1

            arr[i],arr[j]=arr[j],arr[i]
    arr[i+1],arr[high] = arr[high],arr[i+1]


    return i+1