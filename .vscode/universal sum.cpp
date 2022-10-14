
#include<iostream>
using namespace std;
int main(){

int n, remainder, reverse=0;
cout<< "n="; //25
cin>> n;
// while(n!=0)
// {
//     remainder=n%10;                 //rem1=5, rem2=2
//     reverse=reverse*10+remainder;   //reverse1=5,reverse2=52
//     n/=10;                          //n1=2, n2=0 -- the loop end.
    
// }
for (int i = n; i >= 1; i--)
{
    remainder=i%10;//3,21
    reverse=reverse*10+remainder;//321
    i/=10;//121
}

    cout << "Reversed number:" << reverse << endl;
    return 0;

}