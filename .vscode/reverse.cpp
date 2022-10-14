#include<iostream>
#include<algorithm>
#include<string.h>
using namespace std;
int main(){
    string txt = "Toshpulatov Ozodbek";
    reverse(txt.begin(), txt.end());
    cout << "\n" << txt;
}