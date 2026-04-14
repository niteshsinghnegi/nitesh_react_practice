// print all sub array
// #include <iostream>
// using namespace std;

// int main(){
//     int arr[] = {1,2,3,4};
//     int n = 4;

//     for (int start = 0; start < n; start++){
//         for(int end = start; end < n; end++){
            
//             for(int i = start; i <= end; i++){
//                 cout << arr[i] << " ";  
//             }
//             cout << endl;  
//         }
//         cout << endl;
//     }

//     return 0;
// }

// maximum subarray sum by "BRUTE FORCE APROCH "
#include <iostream>
#include <climits>
using namespace std ;
int  main (){
    int n = 7;
    int arr1[]={3,-4,5,4,-1,7,-8};
    int max_sum= INT_MIN;
    for ( int start=0;start<n;start ++){
       int current_sum=0;
       for (int end = start ; end < n ;end++){
        current_sum +=arr1[end];
        max_sum=max(current_sum,max_sum);
        
       }
    }
    cout << "maxsum of subarray is = " << " " << max_sum << " \n";
    
}

// leet code problem 53
#include <iostream>
#include <vector>
#include <climits>
using namespace std;

class Solution {
public:
    int MAX_SUMarray(vector<int> &nums){
        int current_sum = 0, max_sum = INT_MIN;

        for (int value : nums){
            current_sum += value;
            max_sum = max(current_sum, max_sum);

            if (current_sum < 0){
                current_sum = 0;
            }
        }

        return max_sum;
    }
};

int main(){
    vector<int> nums = {3,-4,5,4,-1,7,-8};

    Solution obj;  
    
    cout << obj.MAX_SUMarray(nums);  

    return 0;
}