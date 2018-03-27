//Search char array in a char array
//char dizisi icinde char dizisi arama
#include <iostream>
#include <string.h>
using namespace std;



int index(char *str1, char *str2);

int main(){
    char s1[] = "ornegine";
    
    
    char s2[] ="ne";

    int in = index(s1,s2);
    if(in==-1){
        cout<<"\nAranan string bulunamadi.";
    }
    else{
    cout<<"\nAranan string bulundu. Indeks = "<< in;
    }
    return 1;
}

int index(char *st1, char *st2){
    
    int size1 = strlen(st1);
    int size2 = strlen(st2);
    int j;
    cout<< size2;
    if(size1>=size2)
    {
        for(int i = 0; i<(size1-size2+1); i++){
            cout<<"\nSu anda i = "<<i;
            if(st1[i]==st2[0]){
                j=1;
                while(j<size2){
                    if(st1[i+j]==st2[j]){
                        j++;
                    }
                    else{
                        break;
                    }
                }
                if(j==size2){
                    cout<<"\nString Bulundu. Konumu : "<<i;
                    return i;
                }
                else{
                    j=1;
                }
            }
            
            
        }
    }
    return -1;
}