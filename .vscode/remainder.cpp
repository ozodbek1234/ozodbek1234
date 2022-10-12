#include<iostream>
#include<math.h>
using namespace std;
int main(){
    int n=15, d;
    
    for (int i = 0; i < n; i++)
    {
        for (int j = 1; j <= n; j++)
        {
            cout << (i%2) <<" ";
        }
        cout << endl;
    }
    return 0;
}