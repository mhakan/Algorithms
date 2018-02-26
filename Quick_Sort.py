# A list to sort
arr = [6,10,13,5,8,3,2,11];

#It Sorts and Finds Divide Location
def divide(the_list,start,end):
    
    #First element is used as pivot 
    pivot=the_list[start]
    print("pivot = ",pivot)
    loc = start

    #Find lower elements than pivot
    for i in range(start+1,end):
        if (the_list[i]<pivot):
            loc = loc + 1
            tmp = the_list[loc]
            the_list[loc] = the_list[i]
            the_list[i] = tmp
    
    #Locate the pivot        
    tmp = the_list[loc]
    the_list[loc] = the_list[start]
    the_list[start] = tmp
    print("The list after sort at this stage",the_list)
    return loc

#Recursive Quick Sort
def quick_sort(a_list,st,en):
    if st<en:
        location = divide(a_list,st,en)
        quick_sort(a_list,st,location)
        quick_sort(a_list,location+1,en)

#Client Query
print("The list before divide",arr)
quick_sort(arr,0,8)


