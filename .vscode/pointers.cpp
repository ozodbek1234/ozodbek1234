#include<iostream>
using namespace std;
int main(){
    /*int num_1=15, num_2=14;
    int *pointer, *ptr;
    cout << "number one =";
    cin >> num_1;
    pointer=&num_1;
    cout << pointer << endl;// num_1 o'zgaruvchisining xotira manzili
    // adresni 16 lik sanoq tizimida ko'rsatadi
    cout << "number two =";
    cin >> num_2;
    ptr=&num_2;
    cout << ptr << endl;
    */
   
   //2-USUL
   int val=10;
   int *ptr=&val;
   cout << val << endl;
   cout << ptr << endl;
   cout << *ptr << endl;
    return 0;
}