#A sorted list is needed to binary search
my_list = [1, 2, 4, 6, 7, 8, 11, 15, 16, 17, 19, 24, 25, 26, 28, 29]

# The element that be searched
el = 29


def binary_search(m_list, elm):
    middle_point = round(len(m_list)/2)
    print("list is : ", m_list)
    print("middle point element : ", m_list[middle_point])
    if elm == m_list[middle_point]:
        print("Found :", m_list[middle_point])
    else:
        if middle_point <= 0:
            print("This element could not be found in the list")
        else:
            if middle_point != 0:
                if elm < m_list[middle_point]:
                    new_list = m_list[:middle_point]
                else:
                    new_list = m_list[middle_point:]
            binary_search(new_list, elm)


binary_search(my_list, el)
