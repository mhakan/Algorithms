#include <iostream>
using namespace std;

int divide_array(int *, int);
void Quick_Sort(int list[],int s, int e);

int main() 
{
    int arr[] = {6,10,13,5,8,3,2,11};
    cout << "Hello, World! \n";
    //divide_array(arr, 8);
    Quick_Sort(arr,0,7);
    cout<<"\narr= ";
    for (int i = 0; i < 7; i++)
        {
            cout<<"\t"<< arr[i];

        }
    return 0;
}


int divide_array(int *ar,int bas, int len){
    
    int pivot;
    pivot = ar[bas];
    cout<<"\nPIVOT ELEMENT : "<<pivot;
    cout<<"\n bas = "<<bas<<" son = " << len <<"\n";
    cout<<"\n The actual list : \n";
    
    for (int i = bas; i < len; i++)
    {
        cout<<ar[i]<<"\t";
    }
    
    int p_loc = bas;

    int p = 0;

    for (int i = bas+1; i < len; i++)
    {
        if(ar[i]<pivot){
           
            p_loc += 1;
            int tmp;
            tmp = ar[i];
            ar[i] = ar[p_loc];
            ar[p_loc] = tmp;
        }

        p = ar[p_loc];
    }

 

    int tmp;
    tmp = ar[bas];
    ar[bas] = ar[p_loc];
    ar[p_loc] = tmp;

    

    cout<<"\n Sorted list in this stage "<<"\n";
        for (int i = 0; i < len; i++)
        {
            cout<<ar[i]<<"\t";
        }

        return p_loc;
}


void Quick_Sort(int *list,int s, int e){
    int loc;
    if (s<e)
    {
        loc = divide_array(list,s,e);
        cout<<"\nloc = "<<loc;
        Quick_Sort(list,s,loc-1);
        Quick_Sort(list,loc+1,e);
    }
    
 
}