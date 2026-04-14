// #include <iostream>
// using namespace std;
// int main () {
  
//     int arry[5]={1,2,3,4,5};
//      for (int i =0;i<=5-1;i++){
//     cout<<arry[i];
// }
// }

// #include <iostream>
// #include <climits>   // for INT_MAX
// using namespace std;

// int main () {
//     int nums[5] = {4,6,8,9,1};
//     int smallest = INT_MAX;

//     for(int i = 0; i < 5; i++) {   // FIXED
//         if(nums[i] < smallest) {
//             smallest = nums[i];
//         }
//     }

//     cout << smallest;
// }

// #include <iostream>
// #include <climits>
// using namespace std;

// int main () {
//   int nums[] = {3,4,50,56,76};
//   int n = 5;

//   int largest = INT_MIN;
//   int smallest = INT_MAX;

//   int smallest_index = -1;
//   int largest_index = -1;

//   for (int i = 0; i < n; i++) {

//     if(nums[i] > largest) {
//       largest = nums[i];
//       largest_index = i;   // update only here
//     }

//     if(nums[i] < smallest) {
//       smallest = nums[i];
//       smallest_index = i;  // update only here
//     }

//   }

//   cout << "Largest: " << largest << endl;
//   cout << "Smallest: " << smallest << endl;
//   cout << "Index of largest: " << largest_index << endl;
//   cout << "Index of smallest: " << smallest_index << endl;
// }


// arrays in pass by reffersns 
// #include <iostream>
// using namespace std;

// void change (int numbers[],int n){
//     cout<<"infunction ";

// for (int i =0;i<n;i++){
//     numbers[i]=2*numbers[i];
// }
// }


// int main () {
//     int numbers []={2,4,6};
    
//     change(numbers,3);
//     cout<< "main ";
//     for (int i =0;i<3;i++){
//     cout << numbers [i] << " , ";
//     }
// }


//  linear seracgh in array 
// #include <iostream>
// using namespace std;
// int linear_search( int linear [],int n, int target ){
//     for (int i =0 ;i <n;i++){
//         if(linear[i]== target){
//             return i ;
//         }
//     }
//     return -1;
// }


// int main () {
//     int linear[]={2,3,4,5,6,7,8};
//     int n=7;
//     int target= 6;
// cout << linear_search(linear,n,target) << "\n";
// }
    

// reverse an arry 
// #include <iostream>
// using namespace std;
// void revers_arry(int marks [],int n ){
// int start = 0 , end = n-1;

// while (start < end ){
//     swap( marks[start], marks[end]);
//     start ++;
//     end --;

// }
// }

// int main () {
//     int marks[]={33,44,55,6,7,8};
//     int n =6;
//     revers_arry(marks,n);
//     for ( int i =0 ; i < n ; i ++){
//       cout << marks[i] << "  , ";
//     }
//     return 0 ;
// // }

// //  sum of array element 

// #include <iostream>
// using namespace std;

// int sum (int numberr[],int m ){
//     int sum = 0 ;
//     for (int i =0; i<m; i++){
//         sum +=  numberr[i];
//     }
//     return sum ;
// }
// int main () {
//     int numberr[]={1,2,3,4,5};
//     int m = 5;
// int result = sum(numberr, m );
// cout << "sum =" << result;
// }

//  product or arry element 
// #include <iostream>
// using namespace std;

// int multiplication (int numberr[],int m ){
//     int product= 1;
//     for (int i =0; i<m; i++){
//         product *=  numberr[i];
//     }
//     return product ;
// }
// int main () {
//     int numberr[]={1,2,3,4,5};
//     int m = 5;
//     cout << " product = "<< multiplication(numberr,m);
// }

// swappimg the numbers of an arrya max and min 
// #include <iostream>
// #include <climits>
// using namespace std;

// void swapMinMax(int arr[], int n) {
//     int minIndex = 0;
//     int maxIndex = 0;

//     // Step 1: Find min & max index
//     for(int i = 1; i < n; i++) {
//         if(arr[i] < arr[minIndex]) {
//             minIndex = i;
//         }
//         if(arr[i] > arr[maxIndex]) {
//             maxIndex = i;
//         }
//     }

//     // Step 2: Swap
//     int temp = arr[minIndex];
//     arr[minIndex] = arr[maxIndex];
//     arr[maxIndex] = temp;
// }

// int main() {
//     int arr[] = {3, 4, 50, 56, 76};
//     int n = 5;

//     swapMinMax(arr, n);

//     // Print array
//     for(int i = 0; i < n; i++) {
//         cout << arr[i] << " ";
//     }
// }

// print unique value 
#include <iostream>
using namespace std;
void uniqueMinMax(int arr[], int n){
    for (int i =0; i <n; i++){
        int count = 0 ;
        for (int j=0; j<n; j++){

      
        if (arr[i]==arr[j]){
            count++;
        }
    }
    if (count==1){
        cout<< arr[i]<< " ,";
    }
}
}
int main () {
    int arr[]={1,22,3,22,33,33,4,5,555,444,33,23};
    int n =12;
    cout << "unique value is = " << "\n";
    uniqueMinMax(arr,n);
}
