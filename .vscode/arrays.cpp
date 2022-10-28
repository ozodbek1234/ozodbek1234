#include<iostream>
using namespace std;
int main(){
int monthArray[6];
float total=0;
for (int i = 0; i < 6; i++)
{
    cout << "Enter amount for month " << i+1 << ":";
    cin >> monthArray[i];
    total+=monthArray[i];
}
float average = total/6;
float inTwoYears=average*24;
cout << "Total=" << total<< endl;
cout << "average=" << average << endl;
cout << "inTwoYears=" << inTwoYears << endl; 


return 0;
}