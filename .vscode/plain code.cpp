#include<iostream>
using namespace std;
int main(){
    for (int i = 1; i <= 10; i++)
    {
        if (i==5)
        {
            break;
        }
        else 
        if (i==2)
        {
            continue;
        }
        
        cout << i << " ";
        
    }
    
}