def MergeSort(my_list):
    
    #find the index where divide list
    list_len = len(my_list)
    div_len = round(list_len/2)
    print(div_len)
    sub_list1 = []
    sub_list2 = []

    #Recall the method with sub lists untill reach the 1 sized sublists
    if div_len > 0:

        sub_list1 = my_list[0:div_len]
        print(sub_list1)
        MergeSort(sub_list1)

        sub_list2 = my_list[div_len:list_len]
        print(sub_list2)
        MergeSort(sub_list2)
        print()

    sl1 = sub_list1
    sl2 = sub_list2

    print('degerler')
    l1 = len(sl1)
    l2 = len(sl2)
    print(sl1)
    print(sl2)

    i = 0
    j = 0
    k = 0
    #Sort and merge operation
    while (i < l1 and j < l2):

        if (sl1[i] < sl2[j]):
            my_list[k] = sl1[i]
            i = i + 1

        else:
            my_list[k] = sl2[j]
            j = j + 1

        k = k+1

    #If still there is elements in list, it is added the sorted list
    if(i < l1):
        while (i < l1):
            my_list[k] = sl1[i]
            i = i + 1
            k = k+1
    else:
        while (j < l2):
            my_list[k] = sl2[j]
            j = j + 1
            k = k+1

    print(my_list)


samp_list = [8, 7, 6, 5, 4, 3, 2, 1]
print(samp_list)
#Merge([2,1],[4,3])
MergeSort(samp_list)
