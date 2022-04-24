def bsearch(arr, n, start, end):

   
    while start <= end:

        mid = start+ (end - start)//2

        if arr[mid] == n:

            return mid

        elif arr[mid] < n:

            start = mid + 1

        else:
            
             end = mid - 1

    return -1

arr = [13, 24, 37, 49, 56, 65, 74]

n = 74

print("Given Elements are", arr)

print("Element to be found is ", n)

index = bsearch(arr, n, 0, len(arr)-1)

if index != -1:

    print("The Index of the element is " + str(index))

else:

    print("Element Not found")