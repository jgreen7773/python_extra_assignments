arr = [5,3,9,2,5,7,3,1,8,3]
print(arr)
def swap(inserted_list):
    for i in range(0, len(arr)):
        if inserted_list[i] > inserted_list[i+1]:
            inserted_list[i], inserted_list[i+1] = inserted_list[i+1], inserted_list[i]
            print("Swapped")
            print("\n","*"*80)
        else:
            print("No need to swap")

swap(arr)