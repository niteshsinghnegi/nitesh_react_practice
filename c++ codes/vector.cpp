// leet code value 136 : single number 
// #include <iostream>
// #include <vector>
// using namespace std;

// int SingleValue(vector <int> n&ums){
//     int result=0;
//     for (int value :nums){
//         result=  result ^ value;
//     }
//     return result;
// }

// int main (){
//     vector <int> nums={2,3,4,4,3};
//     int ans=SingleValue(  nums);
    
//     cout << ans;
//  }


//  linear serach by using vector 
// #include <iostream>
// #include <vector>
// using namespace std;

// int linear_serach( vector <int>& num1, int &target){
//     for ( int val : num1){
//         if( val== target){
//             return val;
//         }
//     }
    
//  return -1;
// }

// int main(){
//  vector <int > num1={1,2,3,4,5};
//  int target=2;

//  cout << linear_serach(num1,target);
//  return 0 ;

// }

// reverse code in vector 
// #include <iostream>
// #include <vector>
// #include <climits>
// using namespace std;

// void reverse(vector <int> &num2, int &n ){
//     int start= 0 ;
//     int end = n-1;
//     while(start<end){
//         swap(num2[start],num2[end]);;
//         start ++;
//         end --;
//     }
// }
// int main (){
//     vector <int> num2={1,2,3,4};
//     int n = 4;
//     reverse(num2,n );
//     for (int value1 : num2){
//         cout << value1 << " ";
//     }
// }

// changing vector 
// #include <iostream>
// #include <vector>
// using namespace std;

// void changing_vector(vector<int> &num3){  // pass by reference
//     for(int i = 0; i < num3.size(); i++){
//         num3[i] = 2 * num3[i];
//     }
// }

// int main (){
//     vector<int> num3 = {1,2,3,4};

//     changing_vector(num3);
    
//     for(int value2 : num3){
//         cout << value2 << " ";
//     }
// }


// min max using vector 

// #include <iostream>
// #include <vector>
// #include <climits>
// using namespace std;

// int main() {
//     vector<int> num5 = {1,2,3,4};
//     int n = num5.size();

//     int smallest = INT_MAX;
//     int largest = INT_MIN;

//     for (int i = 0; i < n; i++){
//         smallest = min(num5[i], smallest);
//         largest = max(num5[i], largest);
//     }

//     cout << "Smallest: " << smallest << endl;
//     cout << "Largest: " << largest << endl;
// }


//  #include <iostream>
// #include <vector>
// #include <climits>
// using namespace std;

// void min_max(vector <int> &num11){
//     int larger=INT_MIN;
//     int smallest=INT_MAX;
//     for (int value6 : num11){
//         larger = max(value6,larger);
//         smallest= min(value6,smallest);
          

//         }
//         cout << "largernumber=" << larger <<" " << "smallestnumber"<< smallest;
//     }

// int main (){
//     vector<int > num11={1,2,3,4};
//      min_max(num11);
    
    
// }    


// min and max and also wantindex 

#include <iostream>
#include <vector>
#include <climits>
using namespace std;

void min_max(vector<int> &num11){
    int larger = INT_MIN;
    int smallest = INT_MAX;

    int larger_index = -1;
    int smallest_index = -1;

    int index = 0;

    for (int value : num11){
        if (value > larger){
            larger = value;
            larger_index = index;
        }

        if (value < smallest){
            smallest = value;
            smallest_index = index;
        }

        index++;
    }

    cout << "Largest = " << larger << " at index " << larger_index << endl;
    cout << "Smallest = " << smallest << " at index " << smallest_index << endl;
}