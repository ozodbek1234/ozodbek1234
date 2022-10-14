#include<iostream>
#include<algorithm>
#include<string.h>

using namespace std;
int main(){
    int n, remainder, intager;
    string doc="";
    cout << "Enter a number:";
    cin >> n;
    for (int i = n; i >= 1; i/=2)
    {
      remainder = i % 2; 
      string txt = to_string(remainder);
      doc+=txt; 
      
    }
    reverse(doc.begin(), doc.end());
    intager=stoi(doc);
    cout << "Your binary code is:" <<  intager;

    return 0;
}