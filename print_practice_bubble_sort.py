arr = [5,3,9,2,5,7,3,1,8,3]

def bubbleSort(arr):
    count = 0
    for j in range(len(arr)-1):
        print("/n/n", "_"*50, "Iteration", j)
        for i in range(0, len(arr))-1-j:
            count += 1
            # print("\n","*"*80, "\nindex ", i, "value", arr[i])
            print("\n","*"*80, "\ncomparing", arr[i], arr[i+1])
            if arr[i] > arr[i+1]:
                arr[i], arr[i+1] = arr[i+1], arr[i]
                print("Swapped", arr[i], arr[i+1])
                print("array is now", arr)
            else:
                print("No need to swap", arr[i], arr[i+1])
        
        print('# of evaluations', count)
    return arr

print(bubbleSort(arr))