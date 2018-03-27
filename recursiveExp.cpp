//This code snippet returns exponentiation using recursive approach

#include <iostream>

using namespace std;

float ust(int x, int y);

int main(){
    float s;
    s = ust(2,3);
    cout<<s;
     return 1;
}

float ust (int x, int y){
    float sonuc;
    cout<<"\nx = "<<x<<"\ty = "<< y<<"\n";
    if (y<=1){
        sonuc = x;
        return sonuc;
    }
    else{
        sonuc = x*ust(x,y-1);
        return  sonuc;
    }

}